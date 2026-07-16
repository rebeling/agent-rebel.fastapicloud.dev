---
title: "The Gateway as a Security Boundary"
type: architecture
section: Architecture
section_title: Architecture
section_order: 2
nav_order: 6
summary: "Centralizing model access can improve security only when the gateway itself is treated as high-value infrastructure."
status: reviewed
updated: 2026-07-14
tags: ["security", "secrets", "supply-chain"]
related: ["wiki/governance/authentication-and-keys.md", "wiki/guides/production-readiness.md"]
sources: []
---

A gateway may hold provider credentials, receive confidential prompts, enforce user identity, and log outputs. Compromise can expose every connected model account and application.

## Required controls

- private networking or strict ingress controls
- TLS and, where appropriate, mTLS
- short-lived credentials or managed secret integration
- separated admin and inference interfaces
- least-privilege provider credentials
- signed and pinned artifacts
- rapid patching and rollback
- audit logs for keys, policies, users, and configuration
- payload logging disabled or minimized by default
- tenant isolation in cache, metrics, and storage
- denial-of-wallet protections

## Supply-chain posture

Self-hosting shifts responsibility to the operator. Pin versions, verify images, scan dependencies, follow security advisories, and test upgrades. Do not assume open source means lower risk; it means greater inspection and greater operational ownership.
