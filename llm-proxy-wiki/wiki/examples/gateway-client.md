---
title: "Example: OpenAI Client Through a Gateway"
type: example
section: Examples
section_title: Examples
section_order: 9
nav_order: 3
summary: "A minimal Python client that points an OpenAI-compatible SDK at a gateway."
status: reviewed
updated: 2026-07-14
tags: ["example", "python", "openai-compatible"]
related: ["wiki/concepts/provider-abstraction.md", "wiki/guides/migration-from-direct-provider.md"]
sources: []
---

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_GATEWAY_KEY"],
    base_url=os.environ["LLM_GATEWAY_BASE_URL"],
)

response = client.chat.completions.create(
    model="general-fast",
    messages=[
        {"role": "system", "content": "Answer clearly and briefly."},
        {"role": "user", "content": "Explain why a gateway needs bounded retries."},
    ],
)

print(response.choices[0].message.content)
```

The application depends on the virtual model `general-fast`, not a provider-specific model identifier.

## Keep in application code

- request timeout
- request identifier
- user or tenant attribution metadata
- validation of structured outputs
- safe handling of streamed partial responses
- explicit display or logging of the resolved model when required
