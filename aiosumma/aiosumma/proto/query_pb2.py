# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import utils_pb2 as utils__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bquery.proto\x12\x0bsumma.proto\x1a\x0butils.proto\"_\n\x0eSearchResponse\x12\x37\n\x11\x63ollector_outputs\x18\x01 \x03(\x0b\x32\x1c.summa.proto.CollectorOutput\x12\x14\n\x0c\x65lapsed_secs\x18\x02 \x01(\x01\"\x81\x04\n\x05Query\x12,\n\x07\x62oolean\x18\x01 \x01(\x0b\x32\x19.summa.proto.BooleanQueryH\x00\x12(\n\x05match\x18\x02 \x01(\x0b\x32\x17.summa.proto.MatchQueryH\x00\x12(\n\x05regex\x18\x03 \x01(\x0b\x32\x17.summa.proto.RegexQueryH\x00\x12&\n\x04term\x18\x04 \x01(\x0b\x32\x16.summa.proto.TermQueryH\x00\x12*\n\x06phrase\x18\x05 \x01(\x0b\x32\x18.summa.proto.PhraseQueryH\x00\x12(\n\x05range\x18\x06 \x01(\x0b\x32\x17.summa.proto.RangeQueryH\x00\x12$\n\x03\x61ll\x18\x07 \x01(\x0b\x32\x15.summa.proto.AllQueryH\x00\x12\x38\n\x0emore_like_this\x18\x08 \x01(\x0b\x32\x1e.summa.proto.MoreLikeThisQueryH\x00\x12(\n\x05\x62oost\x18\t \x01(\x0b\x32\x17.summa.proto.BoostQueryH\x00\x12;\n\x0f\x64isjunction_max\x18\n \x01(\x0b\x32 .summa.proto.DisjunctionMaxQueryH\x00\x12(\n\x05\x65mpty\x18\x0b \x01(\x0b\x32\x17.summa.proto.EmptyQueryH\x00\x42\x07\n\x05query\"\n\n\x08\x41llQuery\"\x0c\n\nEmptyQuery\">\n\nBoostQuery\x12!\n\x05query\x18\x01 \x01(\x0b\x32\x12.summa.proto.Query\x12\r\n\x05score\x18\x02 \x01(\t\"Q\n\x13\x44isjunctionMaxQuery\x12%\n\tdisjuncts\x18\x01 \x03(\x0b\x32\x12.summa.proto.Query\x12\x13\n\x0btie_breaker\x18\x02 \x01(\t\"\x91\x03\n\x11MoreLikeThisQuery\x12\x10\n\x08\x64ocument\x18\x01 \x01(\t\x12\x1e\n\x11min_doc_frequency\x18\x02 \x01(\x04H\x00\x88\x01\x01\x12\x1e\n\x11max_doc_frequency\x18\x03 \x01(\x04H\x01\x88\x01\x01\x12\x1f\n\x12min_term_frequency\x18\x04 \x01(\x04H\x02\x88\x01\x01\x12\x1c\n\x0fmax_query_terms\x18\x05 \x01(\x04H\x03\x88\x01\x01\x12\x1c\n\x0fmin_word_length\x18\x06 \x01(\x04H\x04\x88\x01\x01\x12\x1c\n\x0fmax_word_length\x18\x07 \x01(\x04H\x05\x88\x01\x01\x12\x12\n\x05\x62oost\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\x12\n\nstop_words\x18\t \x03(\tB\x14\n\x12_min_doc_frequencyB\x14\n\x12_max_doc_frequencyB\x15\n\x13_min_term_frequencyB\x12\n\x10_max_query_termsB\x12\n\x10_min_word_lengthB\x12\n\x10_max_word_lengthB\x08\n\x06_boost\"9\n\x0bPhraseQuery\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04slop\x18\x03 \x01(\r\">\n\nRangeQuery\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.summa.proto.Range\"\x1b\n\nMatchQuery\x12\r\n\x05value\x18\x01 \x01(\t\"W\n\x0f\x42ooleanSubquery\x12!\n\x05occur\x18\x01 \x01(\x0e\x32\x12.summa.proto.Occur\x12!\n\x05query\x18\x02 \x01(\x0b\x32\x12.summa.proto.Query\"@\n\x0c\x42ooleanQuery\x12\x30\n\nsubqueries\x18\x01 \x03(\x0b\x32\x1c.summa.proto.BooleanSubquery\"*\n\nRegexQuery\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\")\n\tTermQuery\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x80\x01\n\x0b\x41ggregation\x12\x30\n\x06\x62ucket\x18\x01 \x01(\x0b\x32\x1e.summa.proto.BucketAggregationH\x00\x12\x30\n\x06metric\x18\x02 \x01(\x0b\x32\x1e.summa.proto.MetricAggregationH\x00\x42\r\n\x0b\x61ggregation\"\xd7\x02\n\x11\x42ucketAggregation\x12.\n\x05range\x18\x01 \x01(\x0b\x32\x1d.summa.proto.RangeAggregationH\x00\x12\x36\n\thistogram\x18\x02 \x01(\x0b\x32!.summa.proto.HistogramAggregationH\x00\x12.\n\x05terms\x18\x03 \x01(\x0b\x32\x1d.summa.proto.TermsAggregationH\x00\x12K\n\x0fsub_aggregation\x18\x04 \x03(\x0b\x32\x32.summa.proto.BucketAggregation.SubAggregationEntry\x1aO\n\x13SubAggregationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.summa.proto.Aggregation:\x02\x38\x01\x42\x0c\n\nbucket_agg\"U\n\x10RangeAggregation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x32\n\x06ranges\x18\x02 \x03(\x0b\x32\".summa.proto.RangeAggregationRange\"e\n\x15RangeAggregationRange\x12\x11\n\x04\x66rom\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x0f\n\x02to\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x10\n\x03key\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_fromB\x05\n\x03_toB\x06\n\x04_key\"\x9d\x02\n\x14HistogramAggregation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x10\n\x08interval\x18\x02 \x01(\x01\x12\x13\n\x06offset\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12\x1a\n\rmin_doc_count\x18\x04 \x01(\x04H\x01\x88\x01\x01\x12\x36\n\x0bhard_bounds\x18\x05 \x01(\x0b\x32\x1c.summa.proto.HistogramBoundsH\x02\x88\x01\x01\x12:\n\x0f\x65xtended_bounds\x18\x06 \x01(\x0b\x32\x1c.summa.proto.HistogramBoundsH\x03\x88\x01\x01\x42\t\n\x07_offsetB\x10\n\x0e_min_doc_countB\x0e\n\x0c_hard_boundsB\x12\n\x10_extended_bounds\"+\n\x0fHistogramBounds\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\"\xbd\x02\n\x10TermsAggregation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x11\n\x04size\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x17\n\nsplit_size\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x19\n\x0csegment_size\x18\x04 \x01(\rH\x02\x88\x01\x01\x12&\n\x19show_term_doc_count_error\x18\x05 \x01(\x08H\x03\x88\x01\x01\x12\x1a\n\rmin_doc_count\x18\x06 \x01(\x04H\x04\x88\x01\x01\x12,\n\x05order\x18\x07 \x01(\x0b\x32\x18.summa.proto.CustomOrderH\x05\x88\x01\x01\x42\x07\n\x05_sizeB\r\n\x0b_split_sizeB\x0f\n\r_segment_sizeB\x1c\n\x1a_show_term_doc_count_errorB\x10\n\x0e_min_doc_countB\x08\n\x06_order\"\xa3\x01\n\x0b\x43ustomOrder\x12!\n\x03key\x18\x01 \x01(\x0b\x32\x12.summa.proto.EmptyH\x00\x12#\n\x05\x63ount\x18\x02 \x01(\x0b\x32\x12.summa.proto.EmptyH\x00\x12\x19\n\x0fsub_aggregation\x18\x03 \x01(\tH\x00\x12!\n\x05order\x18\x04 \x01(\x0e\x32\x12.summa.proto.OrderB\x0e\n\x0corder_target\"\x8d\x01\n\x11MetricAggregation\x12\x32\n\x07\x61verage\x18\x01 \x01(\x0b\x32\x1f.summa.proto.AverageAggregationH\x00\x12.\n\x05stats\x18\x02 \x01(\x0b\x32\x1d.summa.proto.StatsAggregationH\x00\x42\x14\n\x12metric_aggregation\"#\n\x12\x41verageAggregation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\"!\n\x10StatsAggregation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\"\xdd\x01\n\x0b\x42ucketEntry\x12\x1d\n\x03key\x18\x01 \x01(\x0b\x32\x10.summa.proto.Key\x12\x11\n\tdoc_count\x18\x02 \x01(\x04\x12\x45\n\x0fsub_aggregation\x18\x03 \x03(\x0b\x32,.summa.proto.BucketEntry.SubAggregationEntry\x1aU\n\x13SubAggregationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.summa.proto.AggregationResult:\x02\x38\x01\"*\n\x03Key\x12\r\n\x03str\x18\x01 \x01(\tH\x00\x12\r\n\x03\x66\x36\x34\x18\x02 \x01(\x01H\x00\x42\x05\n\x03key\"U\n\x05Range\x12\x0c\n\x04left\x18\x01 \x01(\t\x12\r\n\x05right\x18\x02 \x01(\t\x12\x16\n\x0eincluding_left\x18\x03 \x01(\x08\x12\x17\n\x0fincluding_right\x18\x04 \x01(\x08\"\x9b\x02\n\x10RangeBucketEntry\x12\x1d\n\x03key\x18\x01 \x01(\x0b\x32\x10.summa.proto.Key\x12\x11\n\tdoc_count\x18\x02 \x01(\x04\x12J\n\x0fsub_aggregation\x18\x03 \x03(\x0b\x32\x31.summa.proto.RangeBucketEntry.SubAggregationEntry\x12\x11\n\x04\x66rom\x18\x04 \x01(\x01H\x00\x88\x01\x01\x12\x0f\n\x02to\x18\x05 \x01(\x01H\x01\x88\x01\x01\x1aU\n\x13SubAggregationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.summa.proto.AggregationResult:\x02\x38\x01\x42\x07\n\x05_fromB\x05\n\x03_to\":\n\x05Score\x12\x13\n\tf64_score\x18\x01 \x01(\x01H\x00\x12\x13\n\tu64_score\x18\x02 \x01(\x04H\x00\x42\x07\n\x05score\"%\n\tHighlight\x12\x0c\n\x04\x66rom\x18\x01 \x01(\r\x12\n\n\x02to\x18\x02 \x01(\r\"U\n\x07Snippet\x12\x10\n\x08\x66ragment\x18\x01 \x01(\x0c\x12*\n\nhighlights\x18\x02 \x03(\x0b\x32\x16.summa.proto.Highlight\x12\x0c\n\x04html\x18\x03 \x01(\t\"\xf0\x01\n\x0eScoredDocument\x12\x10\n\x08\x64ocument\x18\x01 \x01(\t\x12!\n\x05score\x18\x02 \x01(\x0b\x32\x12.summa.proto.Score\x12\x10\n\x08position\x18\x03 \x01(\r\x12;\n\x08snippets\x18\x04 \x03(\x0b\x32).summa.proto.ScoredDocument.SnippetsEntry\x12\x13\n\x0bindex_alias\x18\x05 \x01(\t\x1a\x45\n\rSnippetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.summa.proto.Snippet:\x02\x38\x01\";\n\x06Scorer\x12\x13\n\teval_expr\x18\x01 \x01(\tH\x00\x12\x12\n\x08order_by\x18\x02 \x01(\tH\x00\x42\x08\n\x06scorer\"\xa8\x02\n\tCollector\x12\x31\n\x08top_docs\x18\x01 \x01(\x0b\x32\x1d.summa.proto.TopDocsCollectorH\x00\x12\x45\n\x12reservoir_sampling\x18\x02 \x01(\x0b\x32\'.summa.proto.ReservoirSamplingCollectorH\x00\x12,\n\x05\x63ount\x18\x03 \x01(\x0b\x32\x1b.summa.proto.CountCollectorH\x00\x12,\n\x05\x66\x61\x63\x65t\x18\x04 \x01(\x0b\x32\x1b.summa.proto.FacetCollectorH\x00\x12\x38\n\x0b\x61ggregation\x18\x05 \x01(\x0b\x32!.summa.proto.AggregationCollectorH\x00\x42\x0b\n\tcollector\"\xd3\x02\n\x0f\x43ollectorOutput\x12\x37\n\x08top_docs\x18\x01 \x01(\x0b\x32#.summa.proto.TopDocsCollectorOutputH\x00\x12K\n\x12reservoir_sampling\x18\x02 \x01(\x0b\x32-.summa.proto.ReservoirSamplingCollectorOutputH\x00\x12\x32\n\x05\x63ount\x18\x03 \x01(\x0b\x32!.summa.proto.CountCollectorOutputH\x00\x12\x32\n\x05\x66\x61\x63\x65t\x18\x04 \x01(\x0b\x32!.summa.proto.FacetCollectorOutputH\x00\x12>\n\x0b\x61ggregation\x18\x05 \x01(\x0b\x32\'.summa.proto.AggregationCollectorOutputH\x00\x42\x12\n\x10\x63ollector_output\"\x10\n\x0e\x43ountCollector\"%\n\x14\x43ountCollectorOutput\x12\r\n\x05\x63ount\x18\x01 \x01(\r\"/\n\x0e\x46\x61\x63\x65tCollector\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61\x63\x65ts\x18\x02 \x03(\t\"\x94\x01\n\x14\x46\x61\x63\x65tCollectorOutput\x12H\n\x0c\x66\x61\x63\x65t_counts\x18\x01 \x03(\x0b\x32\x32.summa.proto.FacetCollectorOutput.FacetCountsEntry\x1a\x32\n\x10\x46\x61\x63\x65tCountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\";\n\x1aReservoirSamplingCollector\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\"Z\n\x0eRandomDocument\x12\x10\n\x08\x64ocument\x18\x01 \x01(\t\x12!\n\x05score\x18\x02 \x01(\x0b\x32\x12.summa.proto.Score\x12\x13\n\x0bindex_alias\x18\x03 \x01(\t\"Y\n ReservoirSamplingCollectorOutput\x12\x35\n\x10random_documents\x18\x01 \x03(\x0b\x32\x1b.summa.proto.RandomDocument\"\xf7\x01\n\x10TopDocsCollector\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12(\n\x06scorer\x18\x03 \x01(\x0b\x32\x13.summa.proto.ScorerH\x00\x88\x01\x01\x12=\n\x08snippets\x18\x04 \x03(\x0b\x32+.summa.proto.TopDocsCollector.SnippetsEntry\x12\x0f\n\x07\x65xplain\x18\x05 \x01(\x08\x12\x0e\n\x06\x66ields\x18\x06 \x03(\t\x1a/\n\rSnippetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\t\n\x07_scorer\"a\n\x16TopDocsCollectorOutput\x12\x35\n\x10scored_documents\x18\x01 \x03(\x0b\x32\x1b.summa.proto.ScoredDocument\x12\x10\n\x08has_next\x18\x02 \x01(\x08\"\xb0\x01\n\x14\x41ggregationCollector\x12I\n\x0c\x61ggregations\x18\x01 \x03(\x0b\x32\x33.summa.proto.AggregationCollector.AggregationsEntry\x1aM\n\x11\x41ggregationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.summa.proto.Aggregation:\x02\x38\x01\"\xd5\x01\n\x1a\x41ggregationCollectorOutput\x12\\\n\x13\x61ggregation_results\x18\x01 \x03(\x0b\x32?.summa.proto.AggregationCollectorOutput.AggregationResultsEntry\x1aY\n\x17\x41ggregationResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.summa.proto.AggregationResult:\x02\x38\x01\"\x83\x01\n\x11\x41ggregationResult\x12+\n\x06\x62ucket\x18\x01 \x01(\x0b\x32\x19.summa.proto.BucketResultH\x00\x12+\n\x06metric\x18\x02 \x01(\x0b\x32\x19.summa.proto.MetricResultH\x00\x42\x14\n\x12\x61ggregation_result\"\xa8\x01\n\x0c\x42ucketResult\x12)\n\x05range\x18\x01 \x01(\x0b\x32\x18.summa.proto.RangeResultH\x00\x12\x31\n\thistogram\x18\x02 \x01(\x0b\x32\x1c.summa.proto.HistogramResultH\x00\x12)\n\x05terms\x18\x03 \x01(\x0b\x32\x18.summa.proto.TermsResultH\x00\x42\x0f\n\rbucket_result\"=\n\x0bRangeResult\x12.\n\x07\x62uckets\x18\x01 \x03(\x0b\x32\x1d.summa.proto.RangeBucketEntry\"<\n\x0fHistogramResult\x12)\n\x07\x62uckets\x18\x01 \x03(\x0b\x32\x18.summa.proto.BucketEntry\"\x9f\x01\n\x0bTermsResult\x12)\n\x07\x62uckets\x18\x01 \x03(\x0b\x32\x18.summa.proto.BucketEntry\x12\x1b\n\x13sum_other_doc_count\x18\x02 \x01(\x04\x12(\n\x1b\x64oc_count_error_upper_bound\x18\x03 \x01(\x04H\x00\x88\x01\x01\x42\x1e\n\x1c_doc_count_error_upper_bound\"\x84\x01\n\x0cMetricResult\x12\x38\n\rsingle_metric\x18\x01 \x01(\x0b\x32\x1f.summa.proto.SingleMetricResultH\x00\x12)\n\x05stats\x18\x02 \x01(\x0b\x32\x18.summa.proto.StatsResultH\x00\x42\x0f\n\rmetric_result\"2\n\x12SingleMetricResult\x12\x12\n\x05value\x18\x01 \x01(\x01H\x00\x88\x01\x01\x42\x08\n\x06_value\"\xaf\x01\n\x0bStatsResult\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\x12\x0b\n\x03sum\x18\x02 \x01(\x01\x12\x1f\n\x12standard_deviation\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12\x10\n\x03min\x18\x04 \x01(\x01H\x01\x88\x01\x01\x12\x10\n\x03max\x18\x05 \x01(\x01H\x02\x88\x01\x01\x12\x10\n\x03\x61vg\x18\x06 \x01(\x01H\x03\x88\x01\x01\x42\x15\n\x13_standard_deviationB\x06\n\x04_minB\x06\n\x04_maxB\x06\n\x04_avg*+\n\x05Occur\x12\n\n\x06should\x10\x00\x12\x08\n\x04must\x10\x01\x12\x0c\n\x08must_not\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BUCKETAGGREGATION_SUBAGGREGATIONENTRY._options = None
  _BUCKETAGGREGATION_SUBAGGREGATIONENTRY._serialized_options = b'8\001'
  _BUCKETENTRY_SUBAGGREGATIONENTRY._options = None
  _BUCKETENTRY_SUBAGGREGATIONENTRY._serialized_options = b'8\001'
  _RANGEBUCKETENTRY_SUBAGGREGATIONENTRY._options = None
  _RANGEBUCKETENTRY_SUBAGGREGATIONENTRY._serialized_options = b'8\001'
  _SCOREDDOCUMENT_SNIPPETSENTRY._options = None
  _SCOREDDOCUMENT_SNIPPETSENTRY._serialized_options = b'8\001'
  _FACETCOLLECTOROUTPUT_FACETCOUNTSENTRY._options = None
  _FACETCOLLECTOROUTPUT_FACETCOUNTSENTRY._serialized_options = b'8\001'
  _TOPDOCSCOLLECTOR_SNIPPETSENTRY._options = None
  _TOPDOCSCOLLECTOR_SNIPPETSENTRY._serialized_options = b'8\001'
  _AGGREGATIONCOLLECTOR_AGGREGATIONSENTRY._options = None
  _AGGREGATIONCOLLECTOR_AGGREGATIONSENTRY._serialized_options = b'8\001'
  _AGGREGATIONCOLLECTOROUTPUT_AGGREGATIONRESULTSENTRY._options = None
  _AGGREGATIONCOLLECTOROUTPUT_AGGREGATIONRESULTSENTRY._serialized_options = b'8\001'
  _OCCUR._serialized_start=7301
  _OCCUR._serialized_end=7344
  _SEARCHRESPONSE._serialized_start=41
  _SEARCHRESPONSE._serialized_end=136
  _QUERY._serialized_start=139
  _QUERY._serialized_end=652
  _ALLQUERY._serialized_start=654
  _ALLQUERY._serialized_end=664
  _EMPTYQUERY._serialized_start=666
  _EMPTYQUERY._serialized_end=678
  _BOOSTQUERY._serialized_start=680
  _BOOSTQUERY._serialized_end=742
  _DISJUNCTIONMAXQUERY._serialized_start=744
  _DISJUNCTIONMAXQUERY._serialized_end=825
  _MORELIKETHISQUERY._serialized_start=828
  _MORELIKETHISQUERY._serialized_end=1229
  _PHRASEQUERY._serialized_start=1231
  _PHRASEQUERY._serialized_end=1288
  _RANGEQUERY._serialized_start=1290
  _RANGEQUERY._serialized_end=1352
  _MATCHQUERY._serialized_start=1354
  _MATCHQUERY._serialized_end=1381
  _BOOLEANSUBQUERY._serialized_start=1383
  _BOOLEANSUBQUERY._serialized_end=1470
  _BOOLEANQUERY._serialized_start=1472
  _BOOLEANQUERY._serialized_end=1536
  _REGEXQUERY._serialized_start=1538
  _REGEXQUERY._serialized_end=1580
  _TERMQUERY._serialized_start=1582
  _TERMQUERY._serialized_end=1623
  _AGGREGATION._serialized_start=1626
  _AGGREGATION._serialized_end=1754
  _BUCKETAGGREGATION._serialized_start=1757
  _BUCKETAGGREGATION._serialized_end=2100
  _BUCKETAGGREGATION_SUBAGGREGATIONENTRY._serialized_start=2007
  _BUCKETAGGREGATION_SUBAGGREGATIONENTRY._serialized_end=2086
  _RANGEAGGREGATION._serialized_start=2102
  _RANGEAGGREGATION._serialized_end=2187
  _RANGEAGGREGATIONRANGE._serialized_start=2189
  _RANGEAGGREGATIONRANGE._serialized_end=2290
  _HISTOGRAMAGGREGATION._serialized_start=2293
  _HISTOGRAMAGGREGATION._serialized_end=2578
  _HISTOGRAMBOUNDS._serialized_start=2580
  _HISTOGRAMBOUNDS._serialized_end=2623
  _TERMSAGGREGATION._serialized_start=2626
  _TERMSAGGREGATION._serialized_end=2943
  _CUSTOMORDER._serialized_start=2946
  _CUSTOMORDER._serialized_end=3109
  _METRICAGGREGATION._serialized_start=3112
  _METRICAGGREGATION._serialized_end=3253
  _AVERAGEAGGREGATION._serialized_start=3255
  _AVERAGEAGGREGATION._serialized_end=3290
  _STATSAGGREGATION._serialized_start=3292
  _STATSAGGREGATION._serialized_end=3325
  _BUCKETENTRY._serialized_start=3328
  _BUCKETENTRY._serialized_end=3549
  _BUCKETENTRY_SUBAGGREGATIONENTRY._serialized_start=3464
  _BUCKETENTRY_SUBAGGREGATIONENTRY._serialized_end=3549
  _KEY._serialized_start=3551
  _KEY._serialized_end=3593
  _RANGE._serialized_start=3595
  _RANGE._serialized_end=3680
  _RANGEBUCKETENTRY._serialized_start=3683
  _RANGEBUCKETENTRY._serialized_end=3966
  _RANGEBUCKETENTRY_SUBAGGREGATIONENTRY._serialized_start=3464
  _RANGEBUCKETENTRY_SUBAGGREGATIONENTRY._serialized_end=3549
  _SCORE._serialized_start=3968
  _SCORE._serialized_end=4026
  _HIGHLIGHT._serialized_start=4028
  _HIGHLIGHT._serialized_end=4065
  _SNIPPET._serialized_start=4067
  _SNIPPET._serialized_end=4152
  _SCOREDDOCUMENT._serialized_start=4155
  _SCOREDDOCUMENT._serialized_end=4395
  _SCOREDDOCUMENT_SNIPPETSENTRY._serialized_start=4326
  _SCOREDDOCUMENT_SNIPPETSENTRY._serialized_end=4395
  _SCORER._serialized_start=4397
  _SCORER._serialized_end=4456
  _COLLECTOR._serialized_start=4459
  _COLLECTOR._serialized_end=4755
  _COLLECTOROUTPUT._serialized_start=4758
  _COLLECTOROUTPUT._serialized_end=5097
  _COUNTCOLLECTOR._serialized_start=5099
  _COUNTCOLLECTOR._serialized_end=5115
  _COUNTCOLLECTOROUTPUT._serialized_start=5117
  _COUNTCOLLECTOROUTPUT._serialized_end=5154
  _FACETCOLLECTOR._serialized_start=5156
  _FACETCOLLECTOR._serialized_end=5203
  _FACETCOLLECTOROUTPUT._serialized_start=5206
  _FACETCOLLECTOROUTPUT._serialized_end=5354
  _FACETCOLLECTOROUTPUT_FACETCOUNTSENTRY._serialized_start=5304
  _FACETCOLLECTOROUTPUT_FACETCOUNTSENTRY._serialized_end=5354
  _RESERVOIRSAMPLINGCOLLECTOR._serialized_start=5356
  _RESERVOIRSAMPLINGCOLLECTOR._serialized_end=5415
  _RANDOMDOCUMENT._serialized_start=5417
  _RANDOMDOCUMENT._serialized_end=5507
  _RESERVOIRSAMPLINGCOLLECTOROUTPUT._serialized_start=5509
  _RESERVOIRSAMPLINGCOLLECTOROUTPUT._serialized_end=5598
  _TOPDOCSCOLLECTOR._serialized_start=5601
  _TOPDOCSCOLLECTOR._serialized_end=5848
  _TOPDOCSCOLLECTOR_SNIPPETSENTRY._serialized_start=5790
  _TOPDOCSCOLLECTOR_SNIPPETSENTRY._serialized_end=5837
  _TOPDOCSCOLLECTOROUTPUT._serialized_start=5850
  _TOPDOCSCOLLECTOROUTPUT._serialized_end=5947
  _AGGREGATIONCOLLECTOR._serialized_start=5950
  _AGGREGATIONCOLLECTOR._serialized_end=6126
  _AGGREGATIONCOLLECTOR_AGGREGATIONSENTRY._serialized_start=6049
  _AGGREGATIONCOLLECTOR_AGGREGATIONSENTRY._serialized_end=6126
  _AGGREGATIONCOLLECTOROUTPUT._serialized_start=6129
  _AGGREGATIONCOLLECTOROUTPUT._serialized_end=6342
  _AGGREGATIONCOLLECTOROUTPUT_AGGREGATIONRESULTSENTRY._serialized_start=6253
  _AGGREGATIONCOLLECTOROUTPUT_AGGREGATIONRESULTSENTRY._serialized_end=6342
  _AGGREGATIONRESULT._serialized_start=6345
  _AGGREGATIONRESULT._serialized_end=6476
  _BUCKETRESULT._serialized_start=6479
  _BUCKETRESULT._serialized_end=6647
  _RANGERESULT._serialized_start=6649
  _RANGERESULT._serialized_end=6710
  _HISTOGRAMRESULT._serialized_start=6712
  _HISTOGRAMRESULT._serialized_end=6772
  _TERMSRESULT._serialized_start=6775
  _TERMSRESULT._serialized_end=6934
  _METRICRESULT._serialized_start=6937
  _METRICRESULT._serialized_end=7069
  _SINGLEMETRICRESULT._serialized_start=7071
  _SINGLEMETRICRESULT._serialized_end=7121
  _STATSRESULT._serialized_start=7124
  _STATSRESULT._serialized_end=7299
# @@protoc_insertion_point(module_scope)
