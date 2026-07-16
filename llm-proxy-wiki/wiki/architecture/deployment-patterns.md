---
title: "LLM Gateway Deployment Patterns"
type: architecture
section: Architecture
section_title: Architecture
section_order: 2
nav_order: 2
summary: "Common ways to place a gateway between applications and model backends."
status: reviewed
updated: 2026-07-14
tags: ["deployment", "self-hosted", "saas", "kubernetes"]
related: ["wiki/concepts/control-plane-data-plane.md", "wiki/comparisons/deployment-matrix.md"]
sources: []
---

## Managed SaaS

The vendor operates the data and control planes.

**Best for:** small teams, rapid experiments, low operations capacity.  
**Trade-off:** least infrastructure control and an additional data processor.

Examples: OpenRouter, Vercel AI Gateway, Cloudflare AI Gateway.

## Self-hosted service

The team deploys the gateway in its own environment, commonly with Docker or Kubernetes.

**Best for:** private networking, custom integrations, data control.  
**Trade-off:** patching, scaling, storage, and high availability are operator responsibilities.

Examples: LiteLLM, Portkey OSS gateway, Helicone, AISIX.

## Hybrid control plane and private data plane

A managed control plane configures a customer-hosted request path.

**Best for:** enterprise governance with private traffic.  
**Trade-off:** more complex trust and failure boundaries.

Examples: enterprise platform offerings such as TrueFoundry and API gateway vendors.

## Kubernetes-native gateway

Routes and policies are declarative resources near cluster ingress.

**Best for:** platform teams already operating Gateway API, service mesh, or shared ingress.  
**Trade-off:** excessive complexity for a single small application.

Examples: Envoy AI Gateway, Kong, APISIX.

## Sidecar or embedded proxy

A lightweight proxy runs with an application.

**Best for:** local development, isolated credentials, or per-workload policy.  
**Trade-off:** fragmented configuration and observability at scale.
