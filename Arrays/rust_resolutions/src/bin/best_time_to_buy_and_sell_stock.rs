pub fn max_profit(prices: Vec<i32>) -> i32 {
	let mut max_profit = 0;
	
	let mut left: usize = 0;
	let mut right: usize = 0;

	while right >= left && right < prices.len() {
		println!("{},{}", left, right);
		let current_profit = prices[right] - prices[left];
		if current_profit > max_profit {
			max_profit = current_profit;
		}
		// Avanzamos la derecha si esta es mayor porque buscamos más ganancias. Si es menor, significa que nos serviría que se convirtiera 
		// en nuestro left, pues si a la derecha hubiera una ganancia mayor a la inicial, entonces si nuestro left fuera el más pequeño sería mejor.
		if prices[right] >= prices[left] {
			right += 1;
		} else {
			left += 1;
		}
	}
	max_profit
}

pub fn max_profit_mejor(prices: Vec<i32>) -> i32 {
	let mut max_profit = 0;
	let mut min_profit = i32::MAX;

	for &price in prices.iter() {
		min_profit = min_profit.min(price);
		max_profit = max_profit.max(price - min_profit);
	}

	max_profit
}

fn main() {
	let prices = vec![7,1,5,3,6,4];
	let result = max_profit_mejor(prices);
	println!("{}", result);
}