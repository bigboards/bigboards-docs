# Configuration
The second part of the app creation process deals with defining the configuration. The configuration is used to configure the docker containers, but also to link multiple containers together in case a single app would rely on multiple docker containers.

The configuration is stored in a git repository like github or bitbucket and contains the configuration files and resources for all docker containers inside the app. When an app is installed, a git clone will be done to get the contents from the git repository. **Be aware that private git repo's are not supported at the moment**

