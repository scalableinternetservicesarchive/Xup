======================
FunkLoad_ bench report
======================


:date: 2014-12-08 10:10:30
:abstract: Testing the critical path of the lab app
           Bench result of ``Critical.test_critical_path_readonly``: 
           No test description

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2014-12-08 10:10:30
* From: 169-231-109-153.wireless.ucsb.edu
* Test: ``test_Critical.py Critical.test_critical_path_readonly``
* Target server: http://ec2-54-149-127-241.us-west-2.compute.amazonaws.com
* Cycles of concurrent users: [1, 5, 10]
* Cycle duration: 10s
* Sleeptime between request: from 0.0s to 0.5s
* Sleeptime between test case: 0.01s
* Startup delay between thread: 0.01s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.16.1


Bench content
-------------

The test ``Critical.test_critical_path_readonly`` contains: 

* 2 page(s)
* 0 redirect(s)
* 2 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 60 tests
* 137 pages
* 277 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                  1              0.700                  7                  7             0.00%
                  5              2.900                 29                 29             0.00%
                 10              2.400                 24                 24             0.00%
 ================== ================== ================== ================== ==================



Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note that an XML RPC call count like a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  1              1.000          Excellent              1.500              2.000                 15                 15             0.00%              0.116              0.395              1.253              0.119              0.423              0.577              1.253
                  5              1.000          Excellent              6.300             11.000                 63                 63             0.00%              0.104              0.505              1.949              0.115              0.468              1.074              1.354
                 10              0.942          Excellent              5.900             16.000                 59                 59             0.00%              0.110              1.397              5.134              0.161              1.090              3.291              3.590
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Request stats
-------------

The number of **Requests** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*            Rating*                RPS             maxRPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  1              1.000          Excellent              3.100              5.000                 31                 31             0.00%              0.066              0.191              1.253              0.109              0.126              0.234              0.330
                  5              1.000          Excellent             12.600             19.000                126                126             0.00%              0.102              0.252              0.978              0.113              0.213              0.483              0.555
                 10              0.942          Excellent             12.000             26.000                120                120             0.00%              0.110              0.687              3.325              0.167              0.486              1.849              2.186
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **5** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.32s, link: ``/bootstrap/3.2.0/css/bootstrap.min.css``
  ``
* In page 001, Apdex rating: Excellent, avg response time: 0.31s, link: ``/assets/application-61c7d55e81567830684b7378699345b0.css``
  ``
* In page 001, Apdex rating: Excellent, avg response time: 0.22s, get: ``/index``
  `View index`
* In page 002, Apdex rating: Excellent, avg response time: 0.15s, get: ``/upcoming``
  `View upcoming`

Page detail stats
-----------------


PAGE 001: View index
~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/index``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  8                  8             0.00%              0.109              0.117              0.135              0.109              0.117              0.135              0.135
                      5              1.000          Excellent                 34                 34             0.00%              0.102              0.216              0.978              0.107              0.152              0.259              0.915
                     10              1.000          Excellent                 33                 33             0.00%              0.120              0.325              0.861              0.138              0.258              0.587              0.702
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, link, url ``/bootstrap/3.2.0/css/bootstrap.min.css``

     .. image:: request_001.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  8                  8             0.00%              0.066              0.137              0.243              0.066              0.126              0.243              0.243
                      5              1.000          Excellent                 32                 32             0.00%              0.155              0.323              0.796              0.188              0.290              0.498              0.684
                     10              0.859               Good                 32                 32             0.00%              0.249              1.181              3.325              0.439              1.110              2.190              2.297
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 003, link, url ``/assets/application-61c7d55e81567830684b7378699345b0.css``

     .. image:: request_001.003.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  8                  8             0.00%              0.209              0.237              0.330              0.209              0.231              0.330              0.330
                      5              1.000          Excellent                 31                 31             0.00%              0.197              0.314              0.555              0.221              0.267              0.493              0.551
                     10              0.914               Good                 29                 29             0.00%              0.286              0.920              2.365              0.402              0.663              2.145              2.186
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 002: View upcoming
~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/upcoming``

     .. image:: request_002.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  7                  7             0.00%              0.116              0.286              1.253              0.116              0.122              1.253              1.253
                      5              1.000          Excellent                 29                 29             0.00%              0.104              0.151              0.242              0.108              0.137              0.208              0.216
                     10              1.000          Excellent                 26                 26             0.00%              0.110              0.278              0.808              0.149              0.223              0.578              0.806
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

Definitions
-----------

* CUs: Concurrent users or number of concurrent threads executing tests.
* Request: a single GET/POST/redirect/xmlrpc request.
* Page: a request with redirects and resource links (image, css, js) for an html page.
* STPS: Successful tests per second.
* SPPS: Successful pages per second.
* RPS: Requests per second, successful or not.
* maxSPPS: Maximum SPPS during the cycle.
* maxRPS: Maximum RPS during the cycle.
* MIN: Minimum response time for a page or request.
* AVG: Average response time for a page or request.
* MAX: Maximmum response time for a page or request.
* P10: 10th percentile, response time where 10 percent of pages or requests are delivered.
* MED: Median or 50th percentile, response time where half of pages or requests are delivered.
* P90: 90th percentile, response time where 90 percent of pages or requests are delivered.
* P95: 95th percentile, response time where 95 percent of pages or requests are delivered.
* Apdex T: Application Performance Index, 
  this is a numerical measure of user satisfaction, it is based
  on three zones of application responsiveness:

  - Satisfied: The user is fully productive. This represents the
    time value (T seconds) below which users are not impeded by
    application response time.

  - Tolerating: The user notices performance lagging within
    responses greater than T, but continues the process.

  - Frustrated: Performance with a response time greater than 4*T
    seconds is unacceptable, and users may abandon the process.

    By default T is set to 1.5s this means that response time between 0
    and 1.5s the user is fully productive, between 1.5 and 6s the
    responsivness is tolerating and above 6s the user is frustrated.

    The Apdex score converts many measurements into one number on a
    uniform scale of 0-to-1 (0 = no users satisfied, 1 = all users
    satisfied).

    Visit http://www.apdex.org/ for more information.
* Rating: To ease interpretation the Apdex
  score is also represented as a rating:

  - U for UNACCEPTABLE represented in gray for a score between 0 and 0.5 

  - P for POOR represented in red for a score between 0.5 and 0.7

  - F for FAIR represented in yellow for a score between 0.7 and 0.85

  - G for Good represented in green for a score between 0.85 and 0.94

  - E for Excellent represented in blue for a score between 0.94 and 1.

Report generated with FunkLoad_ 1.16.1, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.