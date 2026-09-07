# Hands-on RL-QAS ✍️
![Awesome](https://awesome.re/badge.svg) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

> **Review Paper:** [<u>Akash Kundu</u>, Aritra Sarkar, Prayag Tiwari, and <u>Sebastian Feld</u>. "Reinforcement Learning for Quantum Circuit Optimization: A Review." Openreview (2026).](https://openreview.net/forum?id=h6w1j1fjeZ)

> **Star (⭐️) my open-source QAS Repo:** [Awesome-QAS](https://github.com/Aqasch/awesome-QAS)

> **The Schedule @ Official Website:** [Website](https://aqasch.github.io/rlqas.github.io/)

<!-- ![RLVTSP](pics/rl-qco-1.png) -->

## RL-QAS Workflow
#### (a) Environment
![RLVTSP](pics/random_2qubit_circuit_single.gif)
<!-- <p style="text-align: center; font-size: 3rem;">↓</p> -->
<p align="center", font-size: 10rem>⬇</p>
<p align="center", font-size: 10rem>⬇</p>
<!-- <p style="text-align: center; font-size: 2rem;">↓</p> -->

#### (b) One Episode
<p align="center">
  <img src="pics/random_2qubit_circuit_group.gif" alt="RLVTSP" width="400">
</p>
<!-- <p style="text-align: center; font-size: 2rem;">↓</p> -->
<p align="center", font-size: 10rem>⬇</p>
<p align="center", font-size: 10rem>⬇</p>

#### (c) Replay buffer
<p align="center">
  <img src="pics/buffer.png" alt="RLVTSP" width="300">
  <!-- tune the focal point: horizontal vertical -->
<img src="pics/buffer_dist.gif" alt="RLVTSP"
     width="400" height="190"
     style="object-fit: cover; object-position: 10% 100%;">
</p>
<!-- <p style="text-align: center; font-size: 2rem;">↓</p> -->
<p align="center", font-size: 10rem>⬇</p>
<p align="center", font-size: 10rem>⬇</p>


#### (d) Sampling from buffer
<p align="center">
  <img src="pics/neural_net.png" alt="RLVTSP" width="300">
</p>
<p align="center", font-size: 10rem>⬇</p>
<p align="center", font-size: 10rem>⬇</p>
<p align="center">
<img src="pics/random_quantum_gate_sampling.gif" alt="RLVTSP"
     width="200">
</p>
<p align="center", font-size: 10rem>⬇</p>
<p align="center", font-size: 10rem>⬇</p>

<p align="center">
  <strong>Goes back to step (a) Environment</strong><br><br>
  <img src="pics/random_2qubit_circuit_group.gif"
       alt="Gate-distribution"
       width="200">
</p>


## IEEE Quantum Week Tutorial on RL-QAS
  <!-- Left logo -->
  <div style="flex: 0 0 auto;">
    <img src="pics/quantum_week_logo.jpg"
         alt="RL-QAS Logo"
         style="height: 80px;">
    <b>T</b>utorial on <b>R</b>einforcement <b>L</b>earning for <b>Q</b>uantum <b>A</b>rchitecture <b>S</b>earch @ <b>Q</b>uantum <b>W</b>eek
    <img src="pics/paper_symbol.png"
         alt="IEEE Quantum Week Logo"
         style="height: 80px;">
  </div>

## The dependencies
```
conda create -n tutorial python=3.10
conda activate tutorial
```

### Install the following few dependencies listed below:

```
pip install notebook
pip install qiskit
pip install qiskit_aer
pip install torch
pip install matplotlib
```

### Open jupyter notebook

On Terminal

```
jupyter notebook
```

## File description

**Noiseless** maximally entangled quantum state preparation:
```
RL-QAS_nonparameterized.ipynb
```

**Noisy** maximally entangled quantum state preparation:
```
RL-QAS_nonparameterized_noise.ipynb
```

Lightweight transfer learning by buffer transfer method:

> **Based on:** [<u>Akash Kundu</u>, and <u>Sebastian Feld</u>. "Replay-buffer engineering for noise-robust quantum circuit optimization." arXiv preprint arXiv:2604.21863 (2026).](https://arxiv.org/abs/2604.21863)

```
RL-QAS_lightweight_buffer_transfer.ipynb
```
