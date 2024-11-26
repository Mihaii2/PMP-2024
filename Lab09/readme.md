# Bayesian Analysis of Store Visits

This analysis examines the posterior distribution of the number of store visits (n) given different observed numbers of purchases (Y) and purchase probabilities (θ).

## Model Structure
- Prior: n ~ Poisson(10)
- Likelihood: Y ~ Binomial(n, θ)

## Effects of Parameters on Posterior Distribution

1. Effect of Y (number of purchases):
   - When Y is low (0), the posterior distribution for n tends to be lower, as few purchases suggest fewer total visitors
   - When Y is high (10), the posterior distribution for n shifts higher, as more purchases necessarily imply more visitors
   - The uncertainty in the posterior (width of distribution) tends to increase with Y

2. Effect of θ (purchase probability):
   - With low θ (0.2), the model infers higher values of n to explain the observed purchases
   - With high θ (0.5), lower values of n can explain the same number of purchases
   - The posterior becomes more concentrated (less uncertain) with higher θ

3. Interaction Effects:
   - The most precise estimates occur with high θ and moderate Y values
   - Extreme combinations (high Y with low θ, or low Y with high θ) lead to more diffuse posteriors
   - The model appropriately handles impossible cases (e.g., Y > n) through the binomial likelihood

This analysis demonstrates how Bayesian inference can combine prior knowledge (Poisson distribution of visits) with observed data (purchases) to estimate the underlying number of store visits.