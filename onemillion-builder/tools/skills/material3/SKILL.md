# Material Design 3 — Design System Reference

This skill provides Material Design 3 (M3) design tokens, component reference, and usage patterns for the design agent.

## M3 Dynamic Color System

One seed color generates the entire palette via the M3 color algorithm.

### Core Token Roles
| Token | Usage |
|-------|-------|
| `--md-sys-color-primary` | Key components, CTAs, active states |
| `--md-sys-color-on-primary` | Text/icons on primary |
| `--md-sys-color-primary-container` | Tonal containers |
| `--md-sys-color-secondary` | Supporting components |
| `--md-sys-color-tertiary` | Accents, highlights |
| `--md-sys-color-surface` | Backgrounds, cards |
| `--md-sys-color-outline` | Borders, dividers |
| `--md-sys-color-error` | Error states |

## MUI Implementation (v6+)

```typescript
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: { main: '#[seed-color]' },
    secondary: { main: '#[secondary]' },
  },
  typography: {
    fontFamily: '[body-font], sans-serif',
    h1: { fontFamily: '[heading-font], sans-serif' },
  },
  shape: { borderRadius: 12 },
});
```

## Component Categories

| Category | Components |
|----------|-----------|
| Buttons | Filled, Outlined, Text, FAB, Icon |
| Cards | Elevated, Filled, Outlined |
| Chips | Assist, Filter, Input, Suggestion |
| Navigation | Nav Bar, Nav Drawer, Nav Rail, Tab Bar |
| Text Fields | Filled, Outlined |
| Dialogs | Basic, Full-screen |
| Lists | List Item, List Item with trailing/leading |

## MCP Tools

If the Material3 MCP server is available, use these tools:
- `list_material_components` — List components by category
- `get_component_code` — Get source code for any component
- `get_design_tokens` — Export tokens in CSS/JSON format
- `search_material_icons` — Search 2,500+ Material Symbols
- `get_accessibility_guidelines` — WCAG 2.1 compliance per component

## Spacing Scale

4px base unit: 4, 8, 12, 16, 24, 32, 48, 64px

## Border Radius Scale

- xs: 4px (chips, small tags)
- sm: 8px (buttons)
- md: 12px (cards, dialogs)
- lg: 16px (containers)
- xl: 28px (large containers)
- full: 50% (avatars, FABs)

## Elevation (Surface Tint Levels)

| Level | Overlay | Use |
|-------|---------|-----|
| 0 | 0% | Base surface |
| 1 | 5% | Card, Switch |
| 2 | 8% | Filled button hover |
| 3 | 11% | FAB |
| 4 | 12% | Navigation drawer |
| 5 | 14% | Bottom sheet |
