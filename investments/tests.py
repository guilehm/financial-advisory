from django.test import Client, TestCase
from model_mommy import mommy

from investments.models import Investment, Equity, Nature, Index, IndexItem


class InvestmentTestCase(TestCase):

    def setUp(self):
        self.nature = mommy.make('investments.Nature')
        self.index = mommy.make('investments.Index')
        self.equity = mommy.make('investments.Equity')
        self.index_item = mommy.make('investments.IndexItem', index=self.index)
        self.investment = mommy.make(
            'investments.Investment', nature=self.nature, index=self.index
        )

    def test_create_nature(self):
        self.assertEquals(Nature.objects.count(), 1)

    def test_create_equity(self):
        self.assertEquals(Equity.objects.count(), 1)

    def test_create_index(self):
        self.assertEquals(Index.objects.count(), 1)

    def test_create_index_item(self):
        self.assertEquals(IndexItem.objects.count(), 1)

    def test_create_investment(self):
        self.assertEquals(Investment.objects.count(), 1)
