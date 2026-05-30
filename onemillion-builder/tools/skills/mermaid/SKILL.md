# Mermaid Diagram Skill

Generate Mermaid diagrams and render them to PNG using mermaid-cli.

## Install

```bash
npm install -g @mermaid-js/mermaid-cli
```

## Render to PNG

```bash
# Write diagram to temp file
cat > /tmp/diagram.mmd << 'EOF'
[mermaid content]
EOF

# Render
npx mmdc -i /tmp/diagram.mmd -o /tmp/diagram.png -t neutral -b transparent
```

## Diagram Types

### System Architecture
```mermaid
graph LR
  Browser --> Vercel
  Vercel --> Railway
  Railway --> Atlas[(MongoDB)]
```

### Data Flow
```mermaid
sequenceDiagram
  Client->>FastAPI: POST /api/v1/auth/login
  FastAPI->>MongoDB: find user by email
  MongoDB-->>FastAPI: user document
  FastAPI-->>Client: {access_token, refresh_token}
```

### Entity Relationship
```mermaid
erDiagram
  User ||--o{ Recipe : owns
  Recipe ||--o{ Comment : has
  Recipe }o--o{ Tag : tagged-with
```

### State Machine
```mermaid
stateDiagram-v2
  [*] --> Idea
  Idea --> Spec
  Spec --> Design
  Design --> Plan
  Plan --> Build
  Build --> Test
  Test --> Guard
  Guard --> Ship
  Ship --> Sell
  Sell --> [*]
```

## In PDF Reports

If mermaid-cli is unavailable, convert diagrams to ASCII box diagrams or structured tables. Never leave raw mermaid code in PDF files.
