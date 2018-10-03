import os
from typing import Dict

from sqla_filters.parser.json import JSONFiltersParser
from sqla_filters.filter import (
    AndNode,
    EqNode,
    NotEqNode,
    NullNode,
    NotNullNode,
    GtNode,
    GteNode,
    LtNode,
    LteNode,
    InNode,
    NotInNode,
    ContainsNode,
    LikeNode
)


class TestParserBase(object):
    _resources: Dict = {}

    def _get_parser(self, key: str) -> JSONFiltersParser:
        """Return a parser instance."""
        file_path = os.path.join(
            os.path.dirname(__file__),
            self._resources[key]
        )
        json_data = open(file_path).read()
        return JSONFiltersParser(json_data)


class TestJsonEquality(TestParserBase):
    def setup_class(self):
        self._resources['eq'] = 'resources/eq/eq.json'
        self._resources['noteq'] = 'resources/eq/noteq.json'
        self._resources['eq_rel'] = 'resources/eq/eq_rel.json'
        self._resources['noteq_rel'] = 'resources/eq/noteq_rel.json'

    def test_01_eq(self):
        parser = self._get_parser('eq')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], EqNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == 'Toto'

    def test_02_noteq(self):
        parser = self._get_parser('noteq')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], NotEqNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == 'Toto'


    def test_03_eq_rel(self):
        parser = self._get_parser('eq_rel')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], EqNode)
        assert parser.tree.root.childs[0].attribute == 'author.person.name'
        assert parser.tree.root.childs[0].value == 'Person_1'

    def test_04_noteq_rel(self):
        parser = self._get_parser('eq_rel')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], EqNode)
        assert parser.tree.root.childs[0].attribute == 'author.person.name'
        assert parser.tree.root.childs[0].value == 'Person_1'


class TestJsonNull(TestParserBase):
    def setup_class(self):
        self._resources['null'] = 'resources/null/null.json'
        self._resources['notnull'] = 'resources/null/notnull.json'

    def test_01_null(self):
        parser = self._get_parser('null')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], NullNode)
        assert parser.tree.root.childs[0].attribute == 'average'
        assert parser.tree.root.childs[0].value == None

    def test_02_notnull(self):
        parser = self._get_parser('notnull')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], NotNullNode)
        assert parser.tree.root.childs[0].attribute == 'average'
        assert parser.tree.root.childs[0].value == None


class TestJsonGreater(TestParserBase):
    def setup_class(self):
        self._resources['gt'] = 'resources/gt/gt.json'
        self._resources['gte'] = 'resources/gt/gte.json'
        self._resources['gt_rel'] = 'resources/gt/gt_rel.json'
        self._resources['gte_rel'] = 'resources/gt/gte_rel.json'

    def test_01_gt(self):
        parser = self._get_parser('gt')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], GtNode)
        assert parser.tree.root.childs[0].attribute == 'age'
        assert parser.tree.root.childs[0].value == 21

    def test_02_gte(self):
        parser = self._get_parser('gte')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], GteNode)
        assert parser.tree.root.childs[0].attribute == 'age'
        assert parser.tree.root.childs[0].value == 21

    def test_03_gt_rel(self):
        parser = self._get_parser('gt_rel')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], GtNode)
        assert parser.tree.root.childs[0].attribute == 'author.posts.pages'
        assert parser.tree.root.childs[0].value == 7

    def test_04_gte_rel(self):
        parser = self._get_parser('gte_rel')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], GteNode)
        assert parser.tree.root.childs[0].attribute == 'author.posts.pages'
        assert parser.tree.root.childs[0].value == 7


class TestJsonLower(TestParserBase):
    def setup_class(self):
        self._resources['lt'] = 'resources/lt/lt.json'
        self._resources['lte'] = 'resources/lt/lte.json'
        self._resources['lt_rel'] = 'resources/lt/lt_rel.json'
        self._resources['lte_rel'] = 'resources/lt/lte_rel.json'

    def test_01_lt(self):
        parser = self._get_parser('lt')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], LtNode)
        assert parser.tree.root.childs[0].attribute == 'age'
        assert parser.tree.root.childs[0].value == 23

    def test_02_lte(self):
        parser = self._get_parser('lte')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], LteNode)
        assert parser.tree.root.childs[0].attribute == 'age'
        assert parser.tree.root.childs[0].value == 23

    def test_03_lt_rel(self):
        parser = self._get_parser('lt_rel')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], LtNode)
        assert parser.tree.root.childs[0].attribute == 'author.posts.pages'
        assert parser.tree.root.childs[0].value == 4

    def test_04_lte_rel(self):
        parser = self._get_parser('lte_rel')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], LteNode)
        assert parser.tree.root.childs[0].attribute == 'author.posts.pages'
        assert parser.tree.root.childs[0].value == 4


class TestJsonIn(TestParserBase):
    def setup_class(self):
        self._resources['in'] = 'resources/in/in.json'
        self._resources['notin'] = 'resources/in/notin.json'
        self._resources['in_rel'] = 'resources/in/in_rel.json'
        self._resources['notin_rel'] = 'resources/in/notin_rel.json'

    def test_01_in(self):
        parser = self._get_parser('in')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], InNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == ['Toto', 'Titi']

    def test_02_notin(self):
        parser = self._get_parser('notin')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], NotInNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == ['Toto', 'Titi']

    def test_03_in_rel(self):
        parser = self._get_parser('in_rel')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], InNode)
        assert parser.tree.root.childs[0].attribute == 'author.person.name'
        assert parser.tree.root.childs[0].value == ['Person_1', 'Person_3']

    def test_04_notin_rel(self):
        parser = self._get_parser('notin_rel')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], NotInNode)
        assert parser.tree.root.childs[0].attribute == 'author.person.name'
        assert parser.tree.root.childs[0].value == ['Person_1', 'Person_3']


class TestJsonContains(TestParserBase):
    def setup_class(self):
        self._resources['contains'] = 'resources/contains/contains.json'

    def test_01_contains(self):
        parser = self._get_parser('contains')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], ContainsNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == 'to'


class TestJsonLike(TestParserBase):
    def setup_class(self):
        self._resources['like_01'] = 'resources/like/like_01.json'
        self._resources['like_02'] = 'resources/like/like_02.json'
        self._resources['like_03'] = 'resources/like/like_03.json'

    def test_01_like(self):
        parser = self._get_parser('like_01')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], LikeNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == 'Pers%'

    def test_02_like(self):
        parser = self._get_parser('like_02')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], LikeNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == '%_1'

    def test_03_like(self):
        parser = self._get_parser('like_03')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], LikeNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == '%son_%'
