======================
FunkLoad_ bench report
======================


:date: 2014-12-03 14:55:27
:abstract: Testing the critical path of the lab app
           Bench result of ``Critical.my_test``: 
           No test description

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2014-12-03 14:55:27
* From: 169-231-102-239.wireless.ucsb.edu
* Test: ``test_Critical.py Critical.my_test``
* Target server: http://ec2-54-149-86-183.us-west-2.compute.amazonaws.com/
* Cycles of concurrent users: [2, 6]
* Cycle duration: 10s
* Sleeptime between request: from 0.0s to 0.5s
* Sleeptime between test case: 0.01s
* Startup delay between thread: 0.01s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.16.1


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

Sorry no test have finished during a cycle, the cycle duration is too short.


Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note that an XML RPC call count like a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  2              0.750               FAIR              0.400              2.000                  4                  4             0.00%              0.477              3.261              6.772              0.477              5.086              6.772              6.772
                  6              0.711               FAIR              0.800              6.000                  8                  8             0.00%              0.638              6.138              8.439              0.638              7.927              8.439              8.439
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
                  2              0.750               FAIR              0.800              2.000                  8                  8             0.00%              0.477              1.631              3.949              0.477              1.632              3.949              3.949
                  6              0.711               FAIR              1.900              6.000                 19                 19             0.00%              0.638              2.584              6.020              0.872              1.576              5.803              6.020
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **2** CUs:

* In page 001, Apdex rating: POOR, avg response time: 3.11s, link: ``/assets/application-61c7d55e81567830684b7378699345b0.css``
  ``
* In page 001, Apdex rating: POOR, avg response time: 1.65s, get: ``//past``
  `View the past page`
* In page 001, Apdex rating: Excellent, avg response time: 1.17s, link: ``/bootstrap/3.2.0/css/bootstrap.min.css``
  ``
* In page 002, Apdex rating: Excellent, avg response time: 0.59s, get: ``/``
  `Get root URL`

Page detail stats
-----------------


PAGE 001: View the past page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``//past``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      2              0.500               POOR                  2                  2             0.00%              1.632              1.649              1.666              1.632              1.666              1.666              1.666
                      6              1.000          Excellent                  6                  6             0.00%              0.872              0.894              0.934              0.872              0.887              0.934              0.934
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, link, url ``/bootstrap/3.2.0/css/bootstrap.min.css``

     .. image:: request_001.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      2              1.000          Excellent                  2                  2             0.00%              1.157              1.168              1.180              1.157              1.180              1.180              1.180
                      6              0.417       UNACCEPTABLE                  6                  6             0.00%              5.190              5.594              6.020              5.190              5.792              6.020              6.020
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 003, link, url ``/assets/application-61c7d55e81567830684b7378699345b0.css``

     .. image:: request_001.003.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      2              0.500               POOR                  2                  2             0.00%              2.274              3.111              3.949              2.274              3.949              3.949              3.949
                      6              0.700               FAIR                  5                  5             0.00%              1.273              1.592              1.849              1.273              1.636              1.849              1.849
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 002: Get root URL
~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/``

     .. image:: request_002.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      2              1.000          Excellent                  2                  2             0.00%              0.477              0.593              0.710              0.477              0.710              0.710              0.710
                      6              0.750               FAIR                  2                  2             0.00%              0.638              1.107              1.576              0.638              1.576              1.576              1.576
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