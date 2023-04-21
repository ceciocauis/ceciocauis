## Open-Source Standard Cell and I/O Cell Design

This repository contains the files of the project *Open-Source Standard Cell and I/O Cell Design*.  
This project was developed by the students **Jhon Pinto** and **Nelson Rodriguez** with the direction of professors **Sebastian Moya** and **Jaime Barrero** at the [**Industrial University of Santander**](https://uis.edu.co/en/)

> The detailed documentation of this project could be read here [paper]

### Standard Cell Library
Student: Nelson Rodriguez

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