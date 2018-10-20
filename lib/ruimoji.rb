# -*- coding: utf-8 -*-

require 'set'

class Ruimoji
  def initialize
    @words = []
    @inv_index = {}
    @min_feat_size = 0
    @max_feat_size = 0
  end

  def serialize(f_path)
    File.open(f_path, 'wb') do |f|
      f.write(Marshal.dump(self))
    end
  end

  def self.load(f_path)
    File.open(f_path, 'rb') do |f|
      Marshal.load(f.read)
    end
  end

  def build_from_file(f_path)
    File.open(f_path) do |f|
      f.each_line do |line|
        registor_word(line.chomp)
      end
      @min_feat_size = @inv_index.keys.min
      @max_feat_size = @inv_index.keys.max
    end
  end

  def build(words)
    words.each do |word|
      registor_word(word)
    end
    @min_feat_size = @inv_index.keys.min
    @max_feat_size = @inv_index.keys.max
  end

  alias :append_words :build

  def append_word(word)
    registor_word(word)
    @min_feat_size = @inv_index.keys.min
    @max_feat_size = @inv_index.keys.max
  end

  def search(q_word, sim_val)
    raise 'invalid sim_val value' unless sim_val > 0.0 and sim_val <= 1.0
    low_b, upp_b = calculate_bound(q_word.size + 1, sim_val)
    low_b = @min_feat_size if low_b < @min_feat_size
    upp_b = @max_feat_size if upp_b > @max_feat_size

    q_feat_set = feature_set(q_word)
    result_indexes = []
    (low_b..upp_b).each do |feat_size|
      teta = min_over_lap(q_feat_set.size, feat_size, sim_val)
      result_indexes.concat(overlap_join(q_feat_set, feat_size, teta))
    end
    result_indexes.map do |w_index|
      @words[w_index].dup
    end
  end

  def search_with_score(q_word, sim_val, sort=true)
    raise 'invalid sim_val value' unless sim_val > 0.0 and sim_val <= 1.0
    low_b, upp_b = calculate_bound(q_word.size + 1, sim_val)
    low_b = @min_feat_size if low_b < @min_feat_size
    upp_b = @max_feat_size if upp_b > @max_feat_size

    q_feat_set = feature_set(q_word)
    result_indexes_with_score = []
    (low_b..upp_b).each do |feat_size|
      teta = min_over_lap(q_feat_set.size, feat_size, sim_val)
      result_indexes_with_score.concat(overlap_join(q_feat_set, feat_size, teta, true))
    end
    result_indexes_with_score.sort_by! {|(w_index, score)| -score } if sort
    result_indexes_with_score.map do |(w_index, score)|
      {:word => @words[w_index].dup, :score => score}
    end
  end

  private

  def registor_word(word)
    word_index = @words.size
    @words << word.dup.freeze

    feat_set = feature_set(word)
    feat_size = feat_set.size
    feat_set.each do |bigram|
      if @inv_index[feat_size].nil?
        @inv_index[feat_size] = {bigram => []}
      elsif @inv_index[feat_size][bigram].nil?
        @inv_index[feat_size][bigram] = []
      end
      @inv_index[feat_size][bigram] << word_index
    end
  end

  def feature_set(word)
    Set.new(
      ("$" + word + "$").each_char.each_cons(2).map do |(c1, c2)|
        c1 + c2
      end
    )
  end

  def calculate_bound(feature_size, sim_val)
    low_b = (feature_size * (sim_val ** 2)).ceil
    upp_b = (feature_size / (sim_val ** 2)).floor
    return low_b, upp_b
  end

  def min_over_lap(feat_size1, feat_size2, sim_val)
    (sim_val * Math.sqrt(feat_size1 * feat_size2)).ceil
  end

  def overlap_join(q_feat_set, feat_size, teta, with_score=false)
    pos_lists = retrieve_pos_lists(q_feat_set, feat_size)
    pos_lists.sort_by! {|pos_list| pos_list.size }

    occ_counter = count_index_occurrence(pos_lists, q_feat_set.size, teta)
    w_indexes = occ_counter.keys
    result_indexes = []
    (q_feat_set.size - teta + 1).upto(q_feat_set.size - 1).each do |i|
      remove_list = []
      w_indexes.each do |w_index|
        if pos_lists[i].bsearch {|idx| w_index - idx }
          occ_counter[w_index] += 1
        end

        if occ_counter[w_index] >= teta and (not with_score)
          result_indexes << w_index
          remove_list << w_index
        elsif occ_counter[w_index] + q_feat_set.size - i + 1 < teta
          remove_list << w_index
        end
      end
      remove_list.each do |remove_i|
        w_indexes.delete(remove_i)
      end
    end
    w_indexes.each do |w_index|
      result_indexes << w_index if occ_counter[w_index] >= teta
    end
    if with_score
      inv_denom = 1.0 / Math.sqrt(q_feat_set.size * feat_size)
      result_indexes.map do |w_index|
        [w_index, occ_counter[w_index] * inv_denom]
      end
    else
      result_indexes
    end
  end

  def retrieve_pos_lists(q_feat_set, feat_size)
    pos_lists = []
    q_feat_set.each do |q_feat|
      if @inv_index[feat_size] and @inv_index[feat_size][q_feat]
        pos_lists << @inv_index[feat_size][q_feat]
      else
        pos_lists << []
      end
    end
    pos_lists
  end

  def count_index_occurrence(pos_lists, q_feat_size, teta)
    counter = Hash.new(0)
    0.upto(q_feat_size - teta).each do |i|
      pos_lists[i].each do |w_index|
        counter[w_index] += 1
      end
    end
    counter
  end
end

if __FILE__ == $0
    ruimoji = Ruimoji.new
words = [
  "スパゲッティー",
  "スパゲッティ",
  "スパゲッテー",
  "スパゲティー",
  "スパッティー",
  "スパゲッティーニ",
  "スパゲッティー・",
  "スパッゲッティー",
  "スパゲッティーニ・",
  "・・スパゲッティー",
  "スープスパゲッティー",
  "スパゲッティーモンスター"
]
ruimoji.build(words) # データベース構築
p ruimoji.search("スパゲティー", 0.7)
# => ["スパゲティー", "スパッティー", "スパゲッティー"]
p ruimoji.search("スパゲティー", 0.6)
# => [
#      "スパゲティー", "スパッティー", "スパゲッティー", "スパッゲッティー", "スパゲッティーニ",
#      "スパゲッティー・", "スープスパゲッティー", "スパゲッティーモンスター"
#    ]
p ruimoji.search_with_score("スパゲティー", 0.7)
# => [
#      {:word=>"スパゲティー", :score=>1.0},
#      {:word=>"スパゲッティー", :score=>0.8017837257372732},
#      {:word=>"スパッティー", :score=>0.7142857142857142}
#    ]
end
