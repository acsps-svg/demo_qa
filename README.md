# demo_qa
It's a repository that contains an basic static HTML page and a front end automation test project that will test the system

# Objective
Show some features that are in Playwright that might be usefull for many Software Tests Engineer. As: codegen, traceview, screenshots etc.

# Codegen

WHile building the automation there's a powerful tool that helps the automation engineer to get locators, and see hoe to claims some actions as click, hover etc. To initiate codegen run the command below.

```playqright codegen```

# Tracing & Trace Viewer 

It's possible to record the tests step by step with th tracing CLI option, is possible to activate that resource adding the flag **--tracing=retain-on-failure** , **on** or **off**
- As an exemple try to run the code below:
```pytest --tracing=retain-on-failure```
If the tests fail a .ZIP file will be generated and with this files we can open the Trace Viewer, running the command below:
```playwright show-trace trace.zip```
