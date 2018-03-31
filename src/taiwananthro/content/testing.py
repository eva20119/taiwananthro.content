# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import taiwananthro.content


class TaiwananthroContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=taiwananthro.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'taiwananthro.content:default')


TAIWANANTHRO_CONTENT_FIXTURE = TaiwananthroContentLayer()


TAIWANANTHRO_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TAIWANANTHRO_CONTENT_FIXTURE,),
    name='TaiwananthroContentLayer:IntegrationTesting'
)


TAIWANANTHRO_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TAIWANANTHRO_CONTENT_FIXTURE,),
    name='TaiwananthroContentLayer:FunctionalTesting'
)


TAIWANANTHRO_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TAIWANANTHRO_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TaiwananthroContentLayer:AcceptanceTesting'
)
