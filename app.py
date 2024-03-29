from tornado import web, ioloop
import json


class ApiHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def get(self, *args):
        self.content_type = 'application/json'

        arguments = self.request.arguments

        if 'chartId' in arguments:
            chartId = int(arguments['chartId'][0])
        else:
            chartId = 1

        response_data = {
            "title": "Active Users Today vs Yesterday",
            "timezone": "Europe\/Madrid",
            "timezone_offset": 3600,
            "legend_enabled": True,
            "series": [
                {
                    "metric": "Today",
                    "name": "Today - mt - fb",
                    "app": "Mailtrack",
                    "platform": "Facebook Canvas",
                    "appPlatformId": "5",
                    "appPlatformTitle": "MT-Fb",
                    "unit": "Users",
                    "dimensions": [],
                    "data": [{"x": 1425168000, "y": 1863367 * chartId},
                             {"x": 1425171600, "y": 127567},
                             {"x": 1425175200, "y": 236608},
                             {"x": 1425178800, "y": 340709},
                             {"x": 1425182400, "y": 433635},
                             {"x": 1425186000, "y": 510654},
                             {"x": 1425189600, "y": 573223},
                             {"x": 1425193200, "y": 628870},
                             {"x": 1425196800, "y": 684045},
                             {"x": 1425200400, "y": 742740},
                             {"x": 1425204000, "y": 804221},
                             {"x": 1425207600, "y": 864805},
                             {"x": 1425211200, "y": 925663},
                             {"x": 1425214800, "y": 989460},
                             {"x": 1425218400, "y": 1057963}
                    ],
                    "serieType": "datetime",
                    "transformations": []
                },
                {
                    "metric": "Yesterday",
                    "name": "Yesterday - mt - fb [cmp]",
                    "app": "Mailtrack",
                    "unit": "Users",
                    "dimensions": [],
                    "data": [{"x": 1425168000, "y": 1863367 / chartId},
                             {"x": 1425171600, "y": 1731251},
                             {"x": 1425175200, "y": 137200},
                             {"x": 1425178800, "y": 252038},
                             {"x": 1425182400, "y": 357786},
                             {"x": 1425186000, "y": 446678},
                             {"x": 1425189600, "y": 521329},
                             {"x": 1425193200, "y": 583867},
                             {"x": 1425196800, "y": 643356},
                             {"x": 1425200400, "y": 705148},
                             {"x": 1425204000, "y": 770596},
                             {"x": 1425207600, "y": 836767},
                             {"x": 1425211200, "y": 901601},
                             {"x": 1425214800, "y": 967255},
                             {"x": 1425218400, "y": 1037015}
                    ],
                    "serieType": "datetime",
                    "transformations": []
                }
            ],
            "flags": [],
            "transformations": []
        }

        response = json.dumps(response_data)
        self.write(response)

    @web.asynchronous
    def post(self):
        pass


class CustomBuilderHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def get(self, *args, **kwargs):
        self.content_type = 'application/json'

        arguments = self.request.arguments

        response_data = [
            [1351728000000,596.54],
            [1351814400000,576.80],
            [1352073600000,584.62],
            [1352160000000,582.85],
            [1352246400000,558.00],
            [1352332800000,537.75],
            [1352419200000,547.06],
            [1352678400000,542.83],
            [1352764800000,542.90],
            [1352851200000,536.88],
            [1352937600000,525.62],
            [1353024000000,527.68],
            [1353283200000,565.73],
            [1353369600000,560.91],
            [1353456000000,561.70],
            [1353628800000,571.50],
            [1353888000000,589.53],
            [1353974400000,584.78],
            [1354060800000,582.94],
            [1354147200000,589.36],
            [1354233600000,585.28],
            # /* Dec 2012
            [1354492800000,586.19],
            [1354579200000,575.85],
            [1354665600000,538.79],
            [1354752000000,547.24],
            [1354838400000,533.25],
            [1355097600000,529.82],
            [1355184000000,541.39],
            [1355270400000,539.00],
            [1355356800000,529.69],
            [1355443200000,509.79],
            [1355702400000,518.83],
            [1355788800000,533.90],
            [1355875200000,526.31],
            [1355961600000,521.73],
            [1356048000000,519.33],
            [1356307200000,520.17],
            [1356480000000,513.00],
            [1356566400000,515.06],
            [1356652800000,509.59],
            [1356912000000,532.17],
            # /* Jan 2013 */
            [1357084800000,549.03],
            [1357171200000,542.10],
            [1357257600000,527.00],
            [1357516800000,523.90],
            [1357603200000,525.31],
            [1357689600000,517.10],
            [1357776000000,523.51],
            [1357862400000,520.30],
            [1358121600000,501.75],
            [1358208000000,485.92],
            [1358294400000,506.09],
            [1358380800000,502.68],
            [1358467200000,500.00],
            [1358812800000,504.77],
            [1358899200000,514.00],
            [1358985600000,450.50],
            [1359072000000,439.88],
            [1359331200000,449.83],
            [1359417600000,458.27],
            [1359504000000,456.83],
            [1359590400000,455.49],
            # /* Feb 2013 */
            [1359676800000,453.62],
            [1359936000000,442.32],
            [1360022400000,457.84],
            [1360108800000,457.35],
            [1360195200000,468.22],
            [1360281600000,474.98],
            [1360540800000,479.93],
            [1360627200000,467.90],
            [1360713600000,467.01],
            [1360800000000,466.59],
            [1360886400000,460.16],
            [1361232000000,459.99],
            [1361318400000,448.85],
            [1361404800000,446.06],
            [1361491200000,450.81],
            [1361750400000,442.80],
            [1361836800000,448.97],
            [1361923200000,444.57],
            [1362009600000,441.40],
            # /* Mar 2013 */
            [1362096000000,430.47],
            [1362355200000,420.05],
            [1362441600000,431.14],
            [1362528000000,425.66],
            [1362614400000,430.58],
            [1362700800000,431.72],
            [1362960000000,437.87],
            [1363046400000,428.43],
            [1363132800000,428.35],
            [1363219200000,432.50],
            [1363305600000,443.66],
            [1363564800000,455.72],
            [1363651200000,454.49],
            [1363737600000,452.08],
            [1363824000000,452.73],
            [1363910400000,461.91],
            [1364169600000,463.58],
            [1364256000000,461.14],
            [1364342400000,452.08],
            [1364428800000,442.66]
        ]
        response = json.dumps({
            'series': [{
                'name': 'test',
                'data': response_data
            }]
        })
        self.write(response)

app = web.Application([
    (r'/api/builder$', CustomBuilderHandler),
    (r'/api$', ApiHandler),
    ],
    debug=True
)

import tornado.platform.twisted
tornado.platform.twisted.install()
from twisted.internet import reactor

import random
import time

from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession

class Component(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        while True:
            value = random.uniform(1, 600)
            timestamp = int(time.time()*1000)
            # timestamp = 1427839684018
            self.publish('com.myapp.test', [timestamp, value])
            yield sleep(1)


if __name__ == '__main__':
    debug = False

    from autobahn.twisted.wamp import ApplicationRunner
    runner = ApplicationRunner("ws://172.17.42.1:8080/ws", "realm1", debug_app=debug, debug_wamp=debug, debug=debug)
    runner.run(Component, start_reactor=False)

    app.listen(8888)
    ioloop.IOLoop.instance().start()
