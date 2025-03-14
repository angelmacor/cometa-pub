# Beer Order Management System - Frontend

This is the frontend application for the Beer Order Management System, built with modern web technologies to provide a seamless user experience for managing beer orders.

## Tech Stack

- **Next.js 13+** - React framework for production
- **TypeScript** - Static type checking
- **Tailwind CSS** - Utility-first CSS framework
- **React Testing Library** - Testing utilities

## Prerequisites

Before you begin, ensure you have installed:
- Node.js (LTS version recommended)
- npm or pnpm (package manager)

## Getting Started

1. Install dependencies:
   ```bash
   pnpm install
   # or
   npm install
   ```

2. Run the development server:
   ```bash
   pnpm dev
   # or
   npm run dev
   ```

3. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Project Structure

```
frontend/
├── src/
│   ├── app/          # App router pages and layouts
│   ├── components/   # Reusable UI components
│   ├── hooks/        # Custom React hooks
│   ├── services/     # API services and data fetching
│   ├── types/        # TypeScript type definitions
│   └── utils/        # Utility functions
├── public/           # Static files
└── tests/           # Test files
```

## Available Scripts

- `pnpm dev` - Starts the development server
- `pnpm build` - Builds the app for production
- `pnpm start` - Runs the built app in production mode
- `pnpm test` - Runs the test suite
- `pnpm lint` - Runs ESLint for code linting

## Development Guidelines

- Follow the TypeScript conventions and maintain type safety
- Use Tailwind CSS for styling components
- Write tests for new components and features
- Follow the existing project structure for new additions

## Testing

We use React Testing Library for component testing. Run tests with:

```bash
pnpm test
```

## Learn More

To learn more about the technologies used:

- [Next.js Documentation](https://nextjs.org/docs)
- [TypeScript Documentation](https://www.typescriptlang.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)
- [React Testing Library Documentation](https://testing-library.com/docs/react-testing-library/intro/)
