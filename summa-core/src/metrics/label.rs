use summa_proto::proto;

pub trait ToLabel {
    fn to_label(&self) -> String;
}

impl ToLabel for proto::Query {
    fn to_label(&self) -> String {
        match &self.query {
            None => "none",
            Some(proto::query::Query::All(_)) => "all",
            Some(proto::query::Query::Boolean(_)) => "boolean",
            Some(proto::query::Query::Empty(_)) => "empty",
            Some(proto::query::Query::Match(_)) => "match",
            Some(proto::query::Query::Range(_)) => "range",
            Some(proto::query::Query::Boost(_)) => "boost",
            Some(proto::query::Query::Regex(_)) => "regex",
            Some(proto::query::Query::Phrase(_)) => "phrase",
            Some(proto::query::Query::Term(_)) => "term",
            Some(proto::query::Query::MoreLikeThis(_)) => "more_like_this",
            Some(proto::query::Query::DisjunctionMax(_)) => "disjunction_max",
        }
        .to_owned()
    }
}
