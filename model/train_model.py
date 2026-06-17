AttributeError
AttributeError: The LogisticRegression model is not compiled. Please run compile(...) first before executing the prediction in FHE.

Traceback (most recent call last)
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/flask/app.py", line 1536, in __call__
return self.wsgi_app(environ, start_response)
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/flask/app.py", line 1514, in wsgi_app
response = self.handle_exception(e)
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/flask/app.py", line 1511, in wsgi_app
response = self.full_dispatch_request()
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/flask/app.py", line 919, in full_dispatch_request
rv = self.handle_user_exception(e)
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/flask/app.py", line 917, in full_dispatch_request
rv = self.dispatch_request()
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/flask/app.py", line 902, in dispatch_request
return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
File "/home/user/adhd_fhe_app/app/routes.py", line 111, in index
fhe_pred = model.predict(input_scaled, fhe="execute")[0]
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/concrete/ml/sklearn/base.py", line 2137, in predict
y_scores = self.decision_function(X, fhe=fhe)
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/concrete/ml/sklearn/base.py", line 2125, in decision_function
y_scores = SklearnLinearModelMixin.predict(self, X, fhe=fhe)
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/concrete/ml/sklearn/base.py", line 814, in predict
self.check_model_is_compiled()
File "/home/user/adhd_fhe_app/venv/lib/python3.10/site-packages/concrete/ml/sklearn/base.py", line 349, in check_model_is_compiled
raise AttributeError(self._is_not_compiled_error_message())
AttributeError: The LogisticRegression model is not compiled. Please run compile(...) first before executing the prediction in FHE.
The debugger caught an exception in your WSGI application. You can now look at the traceback which led to the error.
To switch between the interactive traceback and the plaintext one, you can click on the "Traceback" headline. From the text traceback you can also create a paste of it. For code execution mouse-over the frame you want to debug and click on the console icon on the right side.

You can execute arbitrary Python code in the stack frames and there are some extra helpers available for introspection:

dump() shows all variables in the frame
dump(obj) dumps all that's known about the object
Brought to you by DO