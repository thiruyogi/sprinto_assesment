This project is built on python with selenium and pytest libraries.

Requirements:
Python 3.x
Pip3

Steps to run:
1. Install python 3.x and pip3 in the local.
2. Checkout/clone the repository.
3. Navigate to the project folder in terminal.
4. Run the command 'pip3 install -r requirements.txt' . This will install all the necessary dependencies.
5. Once pip install is completed without any errors run 'pytest'.
6. As we have only on test file that file will run.
7. An HTML report will be generated in the path <project_path>/reports.
8. The cases can run on 3 different browser , with chrome as default. 'pytest --browser_name firefox' this command can be used to run on safari and firefox.

Challenges Faced and mitigation:
1. Clear trip has a rate limit for hitting the url, if any access related error messages are recieved kindly wait for a few minutes and retrigger the automation run.
2. Listing of flights after searching is blocked when the browser is invoked by any tool. Hence I have verified the negative cases in the automation.
3. The commented code in the test/test_ticket_booking.py file can be referred for the actual problem statement.
   
Further enhancements:
1. Journery details hash can be enhanced for accomodating other search criteria like 'round trip, number of passenger and different set of fares'.
2. Captuirng screenshots on failures and attaching to report.
3. Credentials and secrets can be read from config files. As login is not needed Base Url is hardcoded in conftest.py.
