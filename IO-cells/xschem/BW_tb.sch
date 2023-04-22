v {xschem version=3.1.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 100 -250 100 -210 { lab=#net1}
N 660 -250 680 -250 { lab=out}
N 100 -150 100 -90 { lab=GND}
N 360 130 360 150 { lab=GND}
N 680 -250 730 -250 { lab=out}
N 100 130 680 130 {
lab=GND}
N 100 -90 100 130 {
lab=GND}
N 540 -250 660 -250 {
lab=out}
N 190 -230 240 -230 {
lab=GND}
N 190 -230 190 130 {
lab=GND}
N 220 -210 240 -210 {
lab=vdd}
N 220 -210 220 -120 {
lab=vdd}
N 220 -60 220 130 {
lab=GND}
N 220 -150 260 -150 {
lab=vdd}
N 590 -250 590 -110 {
lab=out}
N 590 -50 590 130 {
lab=GND}
N 100 -250 120 -250 {
lab=#net1}
N 180 -250 240 -250 {
lab=in}
N 210 -270 210 -250 {
lab=in}
N 680 -250 680 -110 {
lab=out}
N 680 -50 680 130 {
lab=GND}
C {devices/gnd.sym} 360 150 0 0 {name=l1 lab=GND}
C {devices/code_shown.sym} 400 -330 0 0 {name=s1 only_toplevel=false value=".lib /usr/local/share/pdk/sky130A/libs.tech/ngspice/sky130.lib.spice tt"}
C {devices/code_shown.sym} 430 180 0 0 {name=s2 only_toplevel=false value=".control
ac dec 10 1 1000T
plot db(v(out))
meas ac f0 when v(out)=0.7079

.endc"}
C {devices/opin.sym} 730 -250 0 0 {name=p2 lab=out}
C {devices/opin.sym} 210 -270 3 0 {name=p1 lab=in}
C {devices/vsource.sym} 100 -180 0 0 {name=V2 value="1 AC 1"}
C {Padtest.sym} 390 -230 0 0 {name=x1}
C {devices/vsource.sym} 220 -90 0 0 {name=V1 value=1.8}
C {devices/opin.sym} 260 -150 0 0 {name=p3 lab=vdd}
C {devices/capa.sym} 680 -80 0 0 {name=C1
m=1
value=20p
footprint=1206
device="ceramic capacitor"}
C {devices/res.sym} 590 -80 0 0 {name=R2
value=50
footprint=1206
device=resistor
m=1}
C {devices/res.sym} 150 -250 3 0 {name=R1
value=50
footprint=1206
device=resistor
m=1}
