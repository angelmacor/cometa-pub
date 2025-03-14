import { render, screen } from "@testing-library/react";
import OrdersPage from "./page";
import { useOrder } from "@/hooks/useOrder";
import OrderSummary from "./components/OrderSummary";
import { Order } from "@/types/order"; // Ensure correct import path
import { createRef } from "react";

jest.mock("@/hooks/useOrder");

// Mock OrderSummary component
jest.mock("./components/OrderSummary", () => () => (
  <div data-testid="order-summary" />
));

describe("OrdersPage", () => {
  beforeEach(() => {
    const mockOrder: Order = {
      id: "order-123",
      status: "pending",
      subtotal: 100,
      taxes: 10,
      discounts: 5,
      rounds: [],
    };

    (useOrder as jest.Mock).mockReturnValue({
      loading: false,
      error: null,
      orderRef: createRef<Order>(), 
    });


    (useOrder as jest.Mock).mockReturnValue({
      loading: false,
      error: null,
      orderRef: { current: mockOrder },
    });
  });

  it("renders the title", () => {
    render(<OrdersPage />);
    expect(screen.getByText("Your Cometa Order")).toBeInTheDocument();
  });

  it("shows loading message when loading is true", () => {
    (useOrder as jest.Mock).mockReturnValue({
      loading: true,
      error: null,
      orderRef: { current: null },
    });

    render(<OrdersPage />);
    expect(screen.getByText("Loading order...")).toBeInTheDocument();
  });

  it("displays an error message when an error occurs", () => {
    (useOrder as jest.Mock).mockReturnValue({
      loading: false,
      error: "Error loading order",
      orderRef: { current: null },
    });

    render(<OrdersPage />);
    expect(screen.getByText("Error loading order")).toBeInTheDocument();
  });

  it("renders OrderSummary when there is a valid order", () => {
    render(<OrdersPage />);
    console.log(screen.debug());

    expect(screen.getByTestId("order-summary")).toBeInTheDocument();
  });
});
