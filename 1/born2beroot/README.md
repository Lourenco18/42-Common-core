*This project has been created as part of the 42 curriculum by dasantos*

#

This project focuses on setting up and configuring a secure virtual machine environment. The main goal is to understand the fundamentals of system administration, including operating system installation, user and permission management, security policies, networking, and service configuration.

The virtual machine is configured following strict rules regarding security, services, and system structure, with an emphasis on best practices used in real-world Linux server environments.

## Choice of Operating System

For this project, **Debian** was chosen as the operating system.

### Debian – Pros and Cons

**Pros:**

* Very stable and reliable, widely used on servers
* Large and well-documented package repository
* Strong community support
* Lightweight and well-suited for minimal installations

**Cons:**

* Packages may not be as up-to-date as in rolling-release distributions
* Configuration often requires more manual setup, which may be challenging for beginners

### Rocky Linux – Pros and Cons (Comparison)

**Pros:**

* Binary-compatible with Red Hat Enterprise Linux (RHEL)
* Strong focus on enterprise environments
* SELinux enabled by default, offering advanced security controls

**Cons:**

* Heavier than Debian
* Smaller community compared to Debian
* More complex security configuration for beginners

### Debian vs Rocky Linux

| Aspect      | Debian                    | Rocky Linux        |
| ----------- | ------------------------- | ------------------ |
| Target      | General-purpose / Servers | Enterprise servers |
| Stability   | Very high                 | Very high          |
| Security    | AppArmor                  | SELinux            |
| Ease of use | Easier for beginners      | More complex       |

## Security Modules: AppArmor vs SELinux

**AppArmor (Debian):**

* Profile-based security
* Easier to configure and understand
* Less granular but more user-friendly

**SELinux (Rocky Linux):**

* Label-based security model
* Very powerful and fine-grained control
* Steeper learning curve

## Firewall: UFW vs firewalld

**UFW (Debian):**

* Simple and intuitive
* Ideal for basic firewall configurations
* Easy command-line usage

**firewalld (Rocky Linux):**

* Zone-based management
* More flexible and powerful
* Better suited for complex enterprise setups

## Virtualization Platform: VirtualBox vs UTM

**VirtualBox:**

* Cross-platform (Linux, macOS, Windows)
* Widely used and well-documented
* Ideal for x86_64 architectures

**UTM:**

* Optimized for macOS (especially Apple Silicon)
* Simple interface
* Limited compared to VirtualBox in advanced features

## Main Design Choices

* **Partitioning:** Separate partitions for `/`, `/home`, and swap to improve security and manageability
* **Security Policies:** Use of AppArmor, strong password policies, and limited sudo access
* **User Management:** Creation of a non-root user with controlled sudo privileges
* **Services Installed:** SSH, firewall (UFW), and basic monitoring tools

# Instructions

## Requirements

* VirtualBox or UTM
* Debian (or Rocky Linux) ISO image

## Installation

1. Create a new virtual machine
2. Attach the chosen ISO image
3. Install the operating system following minimal installation guidelines
4. Configure partitions, users, and security settings

## Execution / Usage

* Start the virtual machine
* Connect via terminal or SSH
* Use system commands to manage users, services, and security settings

# Resources

## Technical References

* Debian Documentation: [https://www.debian.org/doc/](https://www.debian.org/doc/)
* Rocky Linux Documentation: [https://docs.rockylinux.org/](https://docs.rockylinux.org/)
* AppArmor Documentation: [https://wiki.ubuntu.com/AppArmor](https://wiki.ubuntu.com/AppArmor)
* SELinux Documentation: [https://selinuxproject.org/](https://selinuxproject.org/)
* UFW Documentation: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
* firewalld Documentation: [https://firewalld.org/documentation/](https://firewalld.org/documentation/)

## AI Usage Disclosure

Artificial Intelligence tools were used to:

* Structure and improve the README documentation
* Clarify comparisons between operating systems and security tools
* Improve clarity and organization of explanations

No AI-generated code was directly included in the system configuration.

---

*This README aims to provide a clear and concise overview of the project for peers, evaluators, and recruiters.*
