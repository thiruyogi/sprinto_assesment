This project is built on Python with selenium and Pytest libraries.

Requirements:
Python 3. x
Pip3

Steps to run:
1. Install python 3.x and pip3 in the local.
2. Checkout/clone the repository.
3. Navigate to the project folder in the terminal.
4. Run the command 'pip3 install -r requirements.txt'. This will install all the necessary dependencies.
5. Once the pip install is completed without any errors run 'pytest'.
6. As we have only one test file that file will run.
7. An HTML report will be generated in the path <project_path>/reports.
8. The cases can run on 3 different browsers, with Chrome as default. 'pytest --browser_name firefox' this command can be used to run on Safari and Firefox.

Challenges Faced and Mitigation:
1. As the Clear Trip application is built on Angular, finding the relative locators was tricky. I tried my best to identify the best possible locators.
2. Clear trip has a rate limit for hitting the URL, if any access-related error messages are received kindly wait for a few minutes and retrigger the automation run.
3. Listing of flights after searching is blocked by the application when the browser is invoked by any tool. I identified this behavior only after writing the complete code, because of the time constraints I couldn't rewrite everything in another application. Hence I have verified the negative cases in the automation.
4. The commented code in the test/test_ticket_booking.py file can be referred to as the solution for the actual problem statement.
   
Further enhancements:
1. Journery details hash can be enhanced for accommodating other search criteria like a round trip, number of passengers, and different sets of fares'.
2. Capturing screenshots of failures and attaching them to the report.
3. Credentials and secrets can be read from config files. As login is not needed Base Url is hardcoded in conftest.py.
