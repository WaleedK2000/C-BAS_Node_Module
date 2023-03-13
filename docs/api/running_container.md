# API Address

api/docker/running_containers

# API Sample Output

````json
{
    "running ": 1,
    "error": "none",
    "data": {
        "amazing_shirley": {
            "Id": "97b2fb236360cc949c8c75a6553f780f42bcbeab540287c74cfa3d3ba877493b",
            "Created": "2023-01-02T12:46:02.9509682Z",
            "Path": "bash",
            "Args": [],
            "State": {
                "Status": "running",
                "Running": true,
                "Paused": false,
                "Restarting": false,
                "OOMKilled": false,
                "Dead": false,
                "Pid": 2827,
                "ExitCode": 0,
                "Error": "",
                "StartedAt": "2023-01-02T12:46:05.306454547Z",
                "FinishedAt": "0001-01-01T00:00:00Z"
            },
            "Image": "sha256:6b7dfa7e8fdbe18ad425dd965a1049d984f31cf0ad57fa6d5377cca355e65f03",
            "ResolvConfPath": "/var/lib/docker/containers/97b2fb236360cc949c8c75a6553f780f42bcbeab540287c74cfa3d3ba877493b/resolv.conf",
            "HostnamePath": "/var/lib/docker/containers/97b2fb236360cc949c8c75a6553f780f42bcbeab540287c74cfa3d3ba877493b/hostname",
            "HostsPath": "/var/lib/docker/containers/97b2fb236360cc949c8c75a6553f780f42bcbeab540287c74cfa3d3ba877493b/hosts",
            "LogPath": "/var/lib/docker/containers/97b2fb236360cc949c8c75a6553f780f42bcbeab540287c74cfa3d3ba877493b/97b2fb236360cc949c8c75a6553f780f42bcbeab540287c74cfa3d3ba877493b-json.log",
            "Name": "/amazing_shirley",
            "RestartCount": 0,
            "Driver": "overlay2",
            "Platform": "linux",
            "MountLabel": "",
            "ProcessLabel": "",
            "AppArmorProfile": "unconfined",
            "ExecIDs": null,
            "HostConfig": {
                "Binds": null,
                "ContainerIDFile": "",
                "LogConfig": {
                    "Type": "json-file",
                    "Config": {}
                },
                "NetworkMode": "default",
                "PortBindings": {},
                "RestartPolicy": {
                    "Name": "no",
                    "MaximumRetryCount": 0
                },
                "AutoRemove": false,
                "VolumeDriver": "",
                "VolumesFrom": null,
                "CapAdd": null,
                "CapDrop": null,
                "CgroupnsMode": "private",
                "Dns": [],
                "DnsOptions": [],
                "DnsSearch": [],
                "ExtraHosts": null,
                "GroupAdd": null,
                "IpcMode": "private",
                "Cgroup": "",
                "Links": null,
                "OomScoreAdj": 0,
                "PidMode": "",
                "Privileged": true,
                "PublishAllPorts": false,
                "ReadonlyRootfs": false,
                "SecurityOpt": [
                    "label=disable"
                ],
                "UTSMode": "",
                "UsernsMode": "",
                "ShmSize": 67108864,
                "Runtime": "runc",
                "ConsoleSize": [
                    0,
                    0
                ],
                "Isolation": "",
                "CpuShares": 0,
                "Memory": 0,
                "NanoCpus": 0,
                "CgroupParent": "",
                "BlkioWeight": 0,
                "BlkioWeightDevice": [],
                "BlkioDeviceReadBps": null,
                "BlkioDeviceWriteBps": null,
                "BlkioDeviceReadIOps": null,
                "BlkioDeviceWriteIOps": null,
                "CpuPeriod": 0,
                "CpuQuota": 0,
                "CpuRealtimePeriod": 0,
                "CpuRealtimeRuntime": 0,
                "CpusetCpus": "",
                "CpusetMems": "",
                "Devices": [],
                "DeviceCgroupRules": null,
                "DeviceRequests": null,
                "KernelMemory": 0,
                "KernelMemoryTCP": 0,
                "MemoryReservation": 0,
                "MemorySwap": 0,
                "MemorySwappiness": null,
                "OomKillDisable": null,
                "PidsLimit": null,
                "Ulimits": null,
                "CpuCount": 0,
                "CpuPercent": 0,
                "IOMaximumIOps": 0,
                "IOMaximumBandwidth": 0,
                "MaskedPaths": null,
                "ReadonlyPaths": null
            },
            "GraphDriver": {
                "Data": {
                    "LowerDir": "/var/lib/docker/overlay2/b752c12aaf53bf7fa74ca94a9171214df6ac43aaca8e0bb80de86ffed23f3d6c-init/diff:/var/lib/docker/overlay2/359000de56b54a8021fdc2d15f7f9d78d64c8a5e488fef8271f4d08f64108a98/diff",
                    "MergedDir": "/var/lib/docker/overlay2/b752c12aaf53bf7fa74ca94a9171214df6ac43aaca8e0bb80de86ffed23f3d6c/merged",
                    "UpperDir": "/var/lib/docker/overlay2/b752c12aaf53bf7fa74ca94a9171214df6ac43aaca8e0bb80de86ffed23f3d6c/diff",
                    "WorkDir": "/var/lib/docker/overlay2/b752c12aaf53bf7fa74ca94a9171214df6ac43aaca8e0bb80de86ffed23f3d6c/work"
                },
                "Name": "overlay2"
            },
            "Mounts": [],
            "Config": {
                "Hostname": "97b2fb236360",
                "Domainname": "",
                "User": "",
                "AttachStdin": true,
                "AttachStdout": true,
                "AttachStderr": true,
                "Tty": true,
                "OpenStdin": true,
                "StdinOnce": true,
                "Env": [
                    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                ],
                "Cmd": [
                    "bash"
                ],
                "Image": "ubuntu",
                "Volumes": null,
                "WorkingDir": "",
                "Entrypoint": null,
                "OnBuild": null,
                "Labels": {}
            },
            "NetworkSettings": {
                "Bridge": "",
                "SandboxID": "f380011b038146dd30f8f8bfdc83a8fb19ca469743dba2911009092d1f199f89",
                "HairpinMode": false,
                "LinkLocalIPv6Address": "",
                "LinkLocalIPv6PrefixLen": 0,
                "Ports": {},
                "SandboxKey": "/var/run/docker/netns/f380011b0381",
                "SecondaryIPAddresses": null,
                "SecondaryIPv6Addresses": null,
                "EndpointID": "4ba4bf48d10ce9c431bda8dc0057de76abfb59f53cb6bb5447f0cfda811f2fdf",
                "Gateway": "172.17.0.1",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "IPAddress": "172.17.0.2",
                "IPPrefixLen": 16,
                "IPv6Gateway": "",
                "MacAddress": "02:42:ac:11:00:02",
                "Networks": {
                    "bridge": {
                        "IPAMConfig": null,
                        "Links": null,
                        "Aliases": null,
                        "NetworkID": "9de1441527d94761bcac14c62dd69e617fa0722dc86fcc181692690a91d894d0",
                        "EndpointID": "4ba4bf48d10ce9c431bda8dc0057de76abfb59f53cb6bb5447f0cfda811f2fdf",
                        "Gateway": "172.17.0.1",
                        "IPAddress": "172.17.0.2",
                        "IPPrefixLen": 16,
                        "IPv6Gateway": "",
                        "GlobalIPv6Address": "",
                        "GlobalIPv6PrefixLen": 0,
                        "MacAddress": "02:42:ac:11:00:02",
                        "DriverOpts": null
                    }
                }
            }
        }
    }
}
```json

