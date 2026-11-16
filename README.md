# BitlifeCrisis (`btlc`)

**A Universal, Sub-Milliwatt, Stateless, Non-Discriminative Bitstream Context Language & Multi-Register Token Engine.**
Universal Stateless Bitstream Context Library designed as a stand-alone core to create any project, portable across Python, Berry, Forth, Lua, eBPF and Subleq.


* **Author & Copyright:** Copyright (c) 2009–2026 Gunther Voet. All Rights Reserved.
* **Community License:** PolyForm Noncommercial License 1.0.0
* **Commercial Inquiries:** `github.gowildchild@xsrv.net` (or open an issue)


## Overview

**BitlifeCrisis (`btlc`)** is a lightweight, zero-trust bytecode specification and execution engine built on pure bitshifting, power-of-2 `IntFlag` matrices and agnostic 32-bit registers (`R0`–`R15`).

Instead of relying on heavy stateful sessions or static bearer tokens, a `btlc` capsule carries its own **execution policy**, **context constraints** and **stateless counter (balanced)** inside a compact binary envelope. When all environmental and structural conditions align, branchless math resolves cleanly to `State.FREE`. If a single bit is tampered with or a boundary constraint fails, execution silently shifts into `State.DEFLECT` (honey-snare) without leaking error states.

### Energy & Compute Efficiency (Sub-Milliwatt Design)

Following the ultra-low-power design philosophy of **Existenz**, `btlc` replaces heavy string parsing, dynamic memory allocation and multi-round cryptographic overhead with deterministic, single-cycle bitwise ALU operations (`AND`, `OR`, `XOR`, `SHL`, `SHR`):

* **Microsecond Execution & Sub-Milliwatt Duty Cycle:** In native compiled ports (`C99`, `Berry`, `Forth`, `eBPF`, `Subleq`), evaluating a multi-register token capsule takes tens of CPU cycles (~0.3–2 µs on 32-bit microcontrollers), allowing edge nodes and ESP32/ARM devices to return immediately to deep sleep with an average continuous draw well below **1 mW (sub-milliwatt)**.
* **Constant 64-Byte Register Footprint:** The entire virtual register bank (`R0`–`R15`) fits inside 64 bytes of stack/cache memory with zero heap allocations.
* **Reference vs. Native Tiers:** `master/btlc_spec.py` serves as the readable Python reference engine and PoC testbed, while `ports/` delivers bare-metal and sub-milliwatt execution across constrained hardware and kernel packet paths.

### Key Architectural Pillars

* **31-Class Orthogonal `IntFlag` Lexicon:** Flattens relational operators, bitwise shifts, arithmetic, spatio-temporal bounds, permissions, and network telemetry into exact power-of-2 bitmasks (`btlc_lexicon.py` / `btlc_lexicon.json`).
* **16 Agnostic 32-Bit Registers (`R0`–`R15`):** Any register can be addressed as a full **32-bit `DOUBLE`**, two **16-bit `WORD`s**, four **8-bit `BYTE`s**, or eight **4-bit `NIBBLE`s** without overwriting adjacent bits.
* **64-Bit (8-Byte) Instruction Atoms:** Fixed-width `>BBBBI` atoms align natively across Python, C99, eBPF, Lua, Forth, Berry, and Subleq.
* **Stateless Counter Equilibrium:** Paired ascending and descending counters (`counter_up + counter_down == Scale - 1`) bounded by configurable power-of-2 scales (`16` to `65536`).

---

## Repository Structure

```text
BitlifeCrisis/
├── LICENSE                         # PolyForm Noncommercial License 1.0.0
├── README.md                       # Project documentation & licensing terms
│
├── master/                         # Canonical Core Specification & Lexicon
│   ├── btlc_spec.py                # Reference Python VM, RegisterBank & Capsule engine
│   ├── btlc_lexicon.py             # Complete 31-class IntFlag lexicon
│   ├── btlc_lexicon.json           # Language-agnostic JSON lexicon for cross-port codegen
│   └── test_vectors/               # Shared hex capsules & expected register states
│
├── ports/                          # Cross-Language ABI Ports (Planned & Active)
│   ├── berry/                      # btlc-berry: Lightweight policy compiler & C99 VM
│   ├── lua/                        # btlc-lua: High-speed register VM for edge/API gateways
│   ├── forth/                      # btlc-forth: Minimal stack/tape dictionary interpreter
│   ├── ebpf/                       # btlc-ebpf: Kernel-level BGP-TACO packet attestation
│   ├── subleq/                     # btlc-subleq: Zero-engine One-Instruction Set runner
│   └── js/                         # btlc.js: Client-side browser decoder for stateless web apps
│
└── pocs/                           # Proofs of Concept & Integrations
    ├── 01_webhook_local_policy/    # Self-validating webhook tokens with embedded subnet locks
    ├── 02_visualmix_bitspace/      # Unified Bit-Space Register compatibility layer
    └── 03_automautist_cards/       # Stateless URL bit-compression for AutoMAutist Assist Cards
```

---

## Quick Start (Python Reference Engine)

Add `master/` to your `PYTHONPATH` (or import directly from your workspace):

```python
from btlc_lexicon import Operators, Compares, Shifts, Datasize
from btlc_spec import BitlifeVM, RegisterBank, Capsule

# 1. Sub-slice a 32-bit register into two 16-bit WORDs
regs = RegisterBank()
regs.write_slice(10, Datasize.WORD, index=1, value=1024)  # High 16 bits
regs.write_slice(10, Datasize.WORD, index=0, value=3071)  # Low 16 bits

# 2. Pack a stateless capsule with a 4096 counter scale
raw_capsule = Capsule.pack_raw(b"\x01\x02\x03\x04", scale=4096)
is_valid, payload, counters = Capsule.unpack_raw(raw_capsule, scale=4096)
```

---

## Licensing & Commercial Rights

* **Community & Non-Commercial Use (PolyForm Noncommercial License 1.0.0):** Free to use, study, port, self-host and modify for personal, educational, research and non-commercial projects. Any network or SaaS deployment of *modified* code must publicly share its source under Section 13 of the license.
* **Commercial & Enterprise Use by Third Parties:** Any commercial deployment, SaaS offering, proprietary integration or commercial hardware/software product by third parties requires a separate paid **Commercial License** from the copyright holder (`github.gowildchild@xsrv.net`).
* **First-Party Commercial Applications:** The copyright holder expressly reserves all rights to develop, distribute, and monetize commercial applications, services, and derivative works built upon this specification and codebase.
