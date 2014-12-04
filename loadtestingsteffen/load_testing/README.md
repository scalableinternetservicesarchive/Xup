
At the end of the course, each team will submit a written report on the
effectiveness of the techniques they have used to improve the
performance and scalability of their project.  The primary tool that will 
be used to test this is called "Funkload".

To get started with funkload, please follow the installation
instructions found here:

http://funkload.nuxeo.org/installation.html

In this directory are a two sample files intended to demonstrate how
Funkload can be used.  Critical.conf contains funkload configuration
parameters.  test_Critcal.py contains two test cases: one that performs
read-only operations, and another that performs a variety of write
operations.


To run the read-only version:
fl-run-bench  test_Critical.py Critical.test_critical_path_readonly

To run the write version:
fl-run-bench  test_Critical.py Critical.test_critical_path

After performing a test, generate an HTML file containing the results:
fl-build-report --html critical-bench.xml


