# -*- coding: utf-8 -*-
from sandhisplitter.postprocessor import PostProcessor
from testtools import TestCase
from sandhisplitter.util import extract


class TestPostProcessor(TestCase):
    def setUp(self):
        super(TestPostProcessor, self).setUp()
        self.PP = PostProcessor()

    def test_splits(self):
        inputs = [
            u'അതിസൗന്ദര്യവും=അതി+സൗന്ദര്യവും|2',
            u'എന്തൊക്കെയുണ്ട്=എന്ത്+ഒക്കെ+ഉണ്ട്|3,9',
            u'കാണാറുണ്ടേ=കാണാറ്+ഉണ്ടേ|4',
            u'പറഞ്ഞുകേൾക്കേണമെന്നുള്ള=പറഞ്ഞുകേൾക്കേണം+എന്ന്+ഉള്ള|14,18',
            u'വായിക്കുമ്പോൾക്കൂടി=വായിക്കുമ്പോൾ+കൂടി|12',
        ]
        for line in inputs:
            (word, splits, locs) = extract(line)
            splits_generated = self.PP.split(word, locs)
            self.assertEqual(splits, splits_generated)
