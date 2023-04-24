## Open-Source Standard Cell and I/O Cell Design

This repository contains the files of the project *Open-Source Standard Cell and I/O Cell Design*.  
This project was developed by the students **Jhon Pinto** and **Nelson Rodriguez** with the direction of professors **Sebastian Moya** and **Jaime Barrero** at the [**Industrial University of Santander**](https://uis.edu.co/en/)

> The detailed documentation of this project could be read here [paper]

### Standard Cell Library  

> Student: **Nelson Rodriguez**    

Ten standard cells were designed and characterized using the [Sky130 PDK](https://skywater-pdk.readthedocs.io/en/main/) and are saved in the folder [standard-cells](./standard-cells/).
1. [INV](./standard-cells/01-inv/)
2. [BUFF](./standard-cells/02-buff/)
3. [NAND2](./standard-cells/03-nand2/)
4. [NOR2](./standard-cells/04-nor2/)
5. [AOI21](./standard-cells/06-oai21/)
6. [OAI21](./standard-cells/06-oai21/)
7. [AOI22](./standard-cells/07-aoi22/)
8. [OAI22](./standard-cells/08-oai22/)
9. [AOI211](./standard-cells/09-aoi211/)
10. [OAI211](./standard-cells/10-oai211/)

Each cell folder contains the following files:
- Layout (`.mag`)
- LEF (`.lef`)
- Extracted Spice model (`.spice`)
- LIB (`.lib`)
- Timing data (`.txt`)

It was developed a set of scripts during the design process and for the cell characterization:  
1. [DSCC](./standard-cells/scripts/dscc/) : Digital Standard Cell Characterization tool.
2. [Fo4](./standard-cells/scripts/fo4/) : Data and post-processing script for the Fo4 testbench.
3. [Grid Template](./standard-cells/scripts/grid-template/) : Script to create custom height grids for layout implementation.
4. [Inverter Chain](./standard-cells/scripts/inverter-chain/) : Data and post-processing scripts for the inverter chain testbench.
5. [Results](./standard-cells/scripts/results/) : Testbench for timing measurements of the inverter designed with the optimal widths obtained.  

### I/O Cells

> Student: **Jhon Pinto**

Three main I/O cells were desiged using the [Sky130 PDK:](https://skywater-pdk.readthedocs.io/en/main/) an analog signal pad cell, filler cell, and cut-off cell and can be found in the folder [IO-cells](https://github.com/ceciocauis/ceciocauis/tree/main/IO-cells). These designes are stored in the following files:

- [cst](https://github.com/ceciocauis/ceciocauis/tree/main/IO-cells/cst): Designs created on the simulation software **[CST Studio Suite software](https://www.3ds.com/es/productos-y-servicios/simulia/productos/cst-studio-suite/)**
- [mag](https://github.com/ceciocauis/ceciocauis/tree/main/IO-cells/mag): Designs created on the VLSI layout tool **[Magic](http://opencircuitdesign.com/magic/)**
- [ngspice](https://github.com/ceciocauis/ceciocauis/tree/main/IO-cells/ngspice): Parasitic extraction files and testbench files runned on the spice simulator **[Ngspice](https://ngspice.sourceforge.io/)**
- [xschem](https://github.com/ceciocauis/ceciocauis/tree/main/IO-cells/xschem): Schematics of the designs created on the capture program **[Xschem](https://xschem.sourceforge.io/stefan/index.html)**

Follows the naming convention for the signal pad cell desings:

<aside>
📄 Sigpad_[”in”NodeSize]_[NumberOfDiodes]
</aside>
