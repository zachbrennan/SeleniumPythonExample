Have to run "pip install selenium" before script will work.
Also need geckodriver. I think I had that installed already.

Was taking REALLY long to run a simple test of the "I'm feeling lucky" button on google (38+ seconds). Found out it is because the page (Ookla speed test) has a shit ton of ads that take forever to load. Didn't notice, because I have adblocker. Selenium waits for the page to load completely before it does anything. Changed the search to "python" and it is way faster now. Not really relevant for our project (unless we run ads?) but figured I'd note it for future use.
