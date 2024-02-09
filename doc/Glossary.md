# Recommended terminology

## General

- <a name="api"></a>**API**
  An application programming interface defines the interactions between multiple software
  intermediaries. They are what Open-CMSIS-Pack components publicly expose for the other components to use.
- <a name="api-extension"></a>**API extension**
  A set of methods and types exposed by a Open-CMSIS-Pack Component expanding the capabilities of another
  Open-CMSIS-Pack component.
- <a name="baremetal"></a>[**Baremetal application**](https://en.wikipedia.org/wiki/Bare_metal)
  **Bare metal** refers to a computer executing instructions directly on logic hardware without an
  intervening operating system. On Cortex-M target this is generally understood as an application
  running in a single thread without task-scheduling. A bare-metal application may still use interrupts.
- <a name="bootstrap"></a>**Bootstrap**
  Bootstrapping is a self-starting process that is supposed to proceed without external input.
  - <a name="app-bootstrap"></a>**Application bootstrap**
    Covers the operation related to the application specific operations such as setup of the
    connectivity stacks as well as the various middleware constituting the application.
  - <a name="dev-bootstrap"></a>**Device bootstrap**
    Covers the operation related to the board/product startup. E.g. clock initialisation, external
    peripheral reset and initialisation.
- <a name="bsp"></a>**BSP** / **Board Support Package**
  A component providing board-specific support.
  This component typically provides through direct implementation or through dependencies, the device
  bootstrap and exposes the device specific features such as functions to get peripherals and/or bus
  instances,  pin multiplexing etc.
- <a name="component"></a>**Components**
    The use of *component* on its own is deprecated because ambiguous. Please use one of those more
    specific forms instead:
  - <a name="api-component"></a>**API component**
    A specialization of a software component that describes an interface. It must also document all
    expected behaviour of the API implementation as well as correct usage of the API.
  - <a name="impl-component"></a>**Implementation Component**
    A component that implements an interface. Such component may export an API extension.)
  - <a name="sw-component"></a>**Software component**
    A software component is a basic building block for the construction of applications. It is a set
    of files, include paths, configurations and dependencies. It can optionally implement one or
    more API.
- <a name="connectivity"></a>**Connectivity**
  Any technology used to interact with entities beyond the device's boundary.
  For example, a UART interface may be considered connectivity when used as a Modbus server endpoint.
- <a name="dependency"></a>**Dependency**
  In context of software components is a relationship where one software component requires anything
  from the other software component or API component or configuration or tool chain or hardware.
- <a name="ext-peripheral"></a>**External peripheral**
  A piece of hardware external to the chip running the code.
  It may be controlled through a hardware-accelerated bus interface or a bit-banged bus interface.
- <a name="host-platform"></a>**Host** / **Host platform**
  A machine running a desktop/server grade OS.
- <a name="hw-platform"></a>**Hardware (HW) Platform**
  A piece of hardware running an embedded application. This can be anything from development kits to
  standalone System on Chips or for example an IoT device.
- <a name="iot-os"></a>**IoT OS**
  A set software stacks typically used by IoT devices and provided by an OS vendor (Mbed, Zephyr,
  AWS FreeRTOS, Azure RTOS, ...). An IoT OS is typically made of a kernel (the RTOS), a connectivity
  stack (IP, BLE etc), a storage stack (block devices, file systems etc) and other middleware.
- <a name="int-peripheral"></a>**Internal** / **On-chip peripheral**
  A piece of hardware internal to the chip running the code.
  It is controlled through the chip memory space.
- <a name="software-pack"></a>**Pack** / **Software Pack**
  A collection of files including a [Pack Description](#pack-desc) file forming
  one or more [Software Component](#component)(s) to be distributed, e.g. as an
  archive or through a [Software Repository](#software-repository).
- <a name="pack-desc"></a>**Pack Description** (PDSC)
  A machine readable file containing meta data for one or more [Software Component](#component)(s)
  maintained and shipped alongside.
- <a name="pack-index"></a>**Pack Index**
  A machine readable index file of available [Pack](#software-pack)s and their according
  origin. The origin can be the location a [Pack](#software-pack) archive can be fetched from
  or a [Software Repository](#software-repository) to refer to.
- <a name="packs-folder"></a>**(Local) Packs Folder**
  A location within an [Application Developer](https://github.com/ARMmbed/Open-CMSIS-Pack-architecture/wiki/Requirements#application-developer)'s
  development environment where [Pack](#software-pack)s are stored to (unarchived).
- <a name="periph-driver"></a>**Peripheral driver** / **Hardware Abstraction Layer (HAL)**
  A piece of software interacting with some piece of hardware either as an *internal peripheral* through the memory bus or as an *external peripheral* through an ADC input, a SPI bus, or an I²C bus.
  In the context of Open-CMSIS-Pack, Peripheral driver and HAL driver are synonyms.
  Examples include:
  - The software driving a CRC hardware acceleration
  - The software driving a sensor, for example an accelerometer
  - The software driving a stepper motor controller
- <a name="rtos"></a>**Real-Time Operating System (RTOS)**
  Part of the OS that implements threading, real-time scheduling and related operations.
  Some well known RTOS for microcontrollers include FreeRTOS (used in AWS-FreeRTOS), RTX (used in Mbed-OS), and ThreadX (used in Azure RTOS).
- <a name="software-repository"></a>**Software Repository**
  Arbitrary directory structure containing files typically version controlled
  by a [VCS](https://en.wikipedia.org/wiki/Version_control).

## Testing

There are two major ways of categorising tests :

- By scope:
  - <a name="unit-test"></a>**Unit tests**
    Covers a specific piece of software isolating it from its environment for example by mocking its dependencies.
    In the case of Internal peripheral drivers that means mocking/simulating the hardware's behaviour and/or memory map.
  - <a name="integration-test"></a>**Integration tests**
    Verifies that multiple components can work together in the expected way.
  - <a name="system-test"></a>[**System tests**](https://en.wikipedia.org/wiki/System_testing)
    Verifies that the components work together as expected and that the whole system also behaves as defined.
- By test objectives:
  - <a name="func-test"></a>[**Functional tests**](https://en.wikipedia.org/wiki/Functional_testing)
  - <a name="api-test"></a>[**API tests**](https://en.wikipedia.org/wiki/API_testing)
  - <a name="stress-test"></a>[**Stress tests**](https://en.wikipedia.org/wiki/Stress_testing)
  - <a name="memory-test"></a>**Memory tests**
    Checks the absence of leaks and buffer overflow.

The following terms are generally accepted and listed here as reminders :

- <a name="acceptance-test"></a>[**Acceptance test**](https://en.wikipedia.org/wiki/Acceptance_testing)
  Tests against design document(s) or specification(s).
- <a name="regression-test"></a>**Regression test**
  Tests that are repeatable and used to catch regressions as the code base evolves.
- **Test framework**
  Library used to help implement a test, e.g. CppUTest
- <a name="test-harness"></a>**Test harness**
  Combination of the Test framework and test data that allow automation of the tests.
- <a name="test-infra"></a>**Test infrastructure**
  Describes the environment where the tests are run. This includes CI and the required HW and SW tools down to the HW Platform boundaries.
- <a name="test-tool"></a>**Test tool**
  Includes the software tools as well as the physical tools such as the FPGA test shield.

## Deprecated terminology

Those terms are not forbidden but frowned upon because of their history, ambiguity and more generally their lack of clarity.

- **Target**
  Has proven ambiguous and highly dependant on the context.
  It may identify a board, a module, a specific chip, a family of device, a core or even a platform or an OS.
  *Recommended alternative*: Use specific wording.
- **Component**
  Similarly to *target* component may indistinctly refer to hardware or software elements.
  *Recommended alternative*: Use specific wording. See [Component](#component).

## System description terminology

This section describes concepts required for describing system on chip (SoC) products, leveraging TrustZone-enabled cores and multi-cores.  
These concepts can also be used more widely to describe multi-SoC systems.  

- <a name="binary-program"></a>**Binary program**
A binary program can be:
  - A bare-metal binary,
  - A monolithic OS binary and all the services running on top of it,
  - An OS that can install modules. Each module can be a binary on its own but still from an execution perspective as the OS is required for this service to run we consider it as a single binary in term of execution context. 
  - A virtual machine or interpreter 
- <a name="execution-context"></a>**Execution Context**
An execution context identifies the “cradle” allowing to run a binary program on a given hardware platform.  
  - A context of execution has a 1-to-1 association to a hardware execution unit. 
  - If we support virtual machines or interpreters, then the virtual machine is associated with one execution context. The programs interpreted by the virtual machine (VM) are stored as data sections in memory, and considered as execution modules within the VM's execution context.
- <a name="execution-domain"></a>**Execution Domain**
An execution domain is a container aggregating all the platform resources (internal and external memories, peripherals) that an execution context can use “exclusively”. For shared resources (available for several execution contexts), we introduce the concept of shared execution domain.
- <a name="execution-module"></a>**Execution Module**
An execution module is an entity that has no standalone execution possibility. It relies on a “backbone" binary providing system services. So, an execution module is always associated with an execution context.
- <a name="HW-exec-unit"></a>**Hardware Execution Unit**
A hardware execution unit is either a cluster (i.e. group of cores), or a core, or a TrustZone world within a core (virtualization). This is the hardware entity (virtual or physical) running a binary program.  
- <a name="SoC"></a>**System On Chip**
A SoC (system on chip) can be a microcontroller (MCU) or a microprocessor (MP). 
  - A SoC can have one or several processors.  
  - A processor can have one or several cores (core = CPU+FPU+…). For example, a Cortex-A7 cluster can have two Cortex-A7 cores.  