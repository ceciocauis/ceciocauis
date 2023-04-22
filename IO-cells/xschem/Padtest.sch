v {xschem version=3.1.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 260 -280 380 -280 {
lab=out}
N 340 -300 380 -300 {
lab=vdd}
N 340 -260 380 -260 {
lab=vss}
N 170 -280 200 -280 {
lab=in}
N 280 -190 290 -190 {
lab=out}
N 280 -280 280 -190 {
lab=out}
C {sky130_fd_pr/res_generic_m5.sym} 230 -280 3 0 {name=R1
W=200
L=2
model=res_generic_m5
mult=1}
C {devices/ipin.sym} 170 -280 0 0 {name=p1 lab=in}
C {devices/opin.sym} 290 -190 0 0 {name=p2 lab=out}
C {devices/ipin.sym} 340 -260 0 0 {name=p3 lab=vss}
C {devices/ipin.sym} 340 -300 0 0 {name=p4 lab=vdd}
C {SigPad.sym} 530 -280 0 0 {name=x1}
