v {xschem version=3.1.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 300 -100 300 -80 {
lab=in}
N 280 20 300 20 {
lab=vss}
N 300 -20 300 20 {
lab=vss}
N 260 -200 300 -200 {
lab=vdd}
N 300 -200 300 -160 {
lab=vdd}
N 210 -90 300 -90 {
lab=in}
C {devices/ipin.sym} 210 -90 0 0 {name=p1 lab=in}
C {devices/ipin.sym} 260 -200 0 0 {name=p3 lab=vdd}
C {devices/ipin.sym} 280 20 0 0 {name=p2 lab=vss}
C {sky130_fd_pr/diode.sym} 300 -130 0 0 {name=D1
model=diode_pd2nw_05v5
area=1000e12
pj=4e6
}
C {sky130_fd_pr/diode.sym} 300 -50 0 0 {name=D2
model=diode_pw2nd_05v5
area=1000e12
pj=4e6
}
