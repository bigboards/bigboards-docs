# Updating your System

There are moments when you want to get to the latest version of the BigBoards
software. We create patches to make the most profound modifications to your
hex. These patches are included inside the `bigboards-updater` application and
they have to be run in a specific order.

But don't worry, that isn't something you should be concerned about. To update
the system, simply run the following command:

```
bb firmware update
```

If your device is running on the _genesis_ version, you will need to [install
the `bb` CLI](migrate.md#installing-the-bb-cli-on-genesis) first.

For the ones of you who do want to dive a bit deeper, we use the
`/opt/bb/.versions` file to determine the current level of the system. Once a
patch is installed a log will be written into this versions file.
