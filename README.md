# prometheus

## Description

This repository contains spec files for building `prometheus` RPM packages and its ecosystem.

Packages are built and published by [spec-package-builder](https://github.com/damex-el-packages/spec-package-builder) pipeline.

Currently, packages and their corresponding spec files are built and tested only for `Red Hat Enterprise Linux 9`, `Red Hat Enterprise Linux 10` and its derivatives like `Alma Linux 9`, `Alma Linux 10`, `Rocky Linux 9` and `Rocky Linux 10`.

[Follow here if you want to use prebuilt packages](#Using-prebuilt-packages).

## Using prebuilt packages

### Add damex-prometheus repository with prebuilt packages

To add `damex-prometheus` repository to `Red Hat Enterprise Linux 9` install the following package:

```sh
# x86_64
https://yum-repositories.damex.org/prometheus/el/9/x86_64/damex-prometheus-release-0.3.0-1.el9.x86_64.rpm
# aarch64
https://yum-repositories.damex.org/prometheus/el/9/aarch64/damex-prometheus-release-0.3.0-1.el9.aarch64.rpm
```

To add `damex-prometheus` repository to `Red Hat Enterprise Linux 10` install the following package:

```sh
# x86_64
https://yum-repositories.damex.org/prometheus/el/10/x86_64/damex-prometheus-release-0.3.0-1.el10.x86_64.rpm
# aarch64
https://yum-repositories.damex.org/prometheus/el/10/aarch64/damex-prometheus-release-0.3.0-1.el10.aarch64.rpm
```

Alternatively, it can be done manually by adding the following configuration to `/etc/yum.repos.d/damex-prometheus.repo`:

```sh
[damex-prometheus]
name = damex-prometheus
baseurl = https://yum-repositories.damex.org/prometheus/el/$releasever/$basearch
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/prometheus/prometheus-2036-09-25.asc
```

### List of prebuilt packages

| Package              | Repository | Architecture | Distributives              |
|----------------------|------------|--------------|----------------------------|
| alertmanager         | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| alertmanager-amtool  | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| blackbox-exporter    | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| jmx-exporter         | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| jmx-exporter-agent   | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kafka-exporter       | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| karma                | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| memcached-exporter   | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| node-exporter        | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| postgresql-exporter  | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| prometheus           | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| prometheus-promtool  | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| redis-exporter       | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| rsyslog-exporter     | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| smartctl-exporter    | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| systemd-exporter     | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| unbound-exporter     | damex-prometheus | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
