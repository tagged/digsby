from facebook import facebookapi
import common.oauth_util as oauth_util

class FacebookAppClient(oauth_util.OAuthClientBase):
    urls = {
        'request_token' : 'https://www.facebook.com/dialog/oauth',
        'access_token'  : 'http://api.myspace.com/access_token',
        'authorization' : 'http://api.myspace.com/authorize',
    }

    @property
    def api(self):
        if getattr(self, '_api', None) is None:
            self._api = facebookapi.FacebookAPI(self)
        return self._api

class DigsbyAppConsumer(oauth_util.OAuthConsumerBase):
    KEY = '5895217474'
    SECRET = 'c0063350ef2fd0b11c2c6869c2c7ef5c'

class DigsbyWidgetAppConsumer(oauth_util.OAuthConsumerBase):
    KEY = '7583798703'
    SECRET = 'd10f42528cc8f39fb04b77b19f911eac'

class DigsbyAchievementsAppConsumer(oauth_util.OAuthConsumerBase):
    KEY = '100249550900'
    SECRET = '33abf1d7cf93cccf494627020d08ceee'

class DigsbyApp(FacebookAppClient):
    name = 'digsby'
    ConsumerFactory = DigsbyAppConsumer

    required_permissions = ['read_stream', 'user_events', 'xmpp_login', 'manage_notifications']
    desired_permissions = required_permissions + ['publish_stream']

class DigsbyWidgetApp(FacebookAppClient):
    name = 'digsby_widget'
    ConsumerFactory = DigsbyWidgetAppConsumer

class DigsbyAchievementsApp(FacebookAppClient):
    name = 'digsby_ach'
    ConsumerFactory = DigsbyAchievementsAppConsumer

    required_permissions = ['publish_stream']
    desired_permissions = required_permissions


