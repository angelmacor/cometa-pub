export interface Beer {
    nameId: string;
    name: string;
    price: number;
    quantity?: number;
  }

  export interface OrderItemDetail {
    name: string;
    quantity: number;
    price_per_unit: number;
    total_price: number;
    subtotal: number;
    discounts: number;
  }
  
  export interface OrderAdd {
    nameId: string;
    name: string;
    quantity: number;
    price: number;

  }

  export interface OrderRound {
    items: OrderItemDetail[];
    created: string;
  }
  
  export interface Order {
    id: string;
    status: 'pending' | 'paid';
    subtotal: number;
    taxes: number;
    discounts: number;
    rounds: OrderRound[];
  }
  
  export interface Stock {
    last_updated: string;
    beers: Beer[];
  }
  