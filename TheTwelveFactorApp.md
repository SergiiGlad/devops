https://12factor.net/uk/

1. __Codebase__: Manage all code in version control systems (like Git or
Mercurial). The codebase comprehensively dictates what is deployed.
2. __Dependencies__: Dependencies should be managed entirely and
explicitly by the codebase, either vendored (stored with the code) or
version pinned in a format that a package manager can install from.
3. __Config__: Separate configuration parameters from the application and
define them in the deployment environment instead of baking them
into the application itself.
4. __Backing services__: Local and remote services are both abstracted as
network-accessible resources with connection details set in
configuration.
5. __Build, release, run__: The build stage of your application should be
completely separate from your application release and operations
processes. The build stage creates a deployment artifact from source
code, the release stage combines the artifact and configuration, and
the run stage executes the release.
6. __Processes__: Applications are implemented as processes that should not
rely on storing state locally. State should be offloaded to a backing
service as described in the fourth factor.
7. __Port binding__: Applications should natively bind to a port and listen
for connections. Routing and request forwarding should be handled
externally.
8. __Concurrency__: Applications should rely on scaling through the process
model. Running multiple copies of an application concurrently,
potentially across multiple servers, allows scaling without adjusting
application code.
9. __Disposability__: Processes should be able to start quickly and stop
gracefully without serious side effects.
10. __Dev/prod parity__: Your testing, staging, and production environments
should match closely and be kept in sync. Differences between
environments are opportunities for incompatibilities and untested
configurations to appear.
11. __Logs__: Applications should stream logs to standard output so external
services can decide how to best handle them.
12. __Admin processes__: One-off administration processes should be run
against specific releases and shipped with the main process code.
