This package can be used to notify the developers about the unhandled exceptions in the code.

When the user of the application faces an error, the developers will be notified and also provided with stacktrace, local variables content needed to debug the issues faster

USAGE: 

	To install: pip install flaskErrorHandler

	Import and initialize with flask app instance

	from flaskErrorHandler import SafeRun

	SafeRun(<<Flask APP Instance>>,{'from_addr':<<FROM ADDRESS>>,'to_addr':<<TO ADDRESS>>,'password':<<FROM ADDRESS GMAIL PASSWORD>>})

