%% Reversible voltage parameters
E0 = 1.229;          % V, reversible voltage at T0
T0 = 298.15;         % K, reference temperature
alpha = -8.5e-4;     % V/K, temperature coefficient

%% Ohmic loss & aging parameters
R0_init = 0.2;       % Ohm, initial resistance
beta = -0.02;        % 1/K, temperature coefficient of resistance
k_deg = 1e-7;        % Ohm/(A*s), degradation rate constant

t = [0 1000 2000 3000 4000];
I = [0 50 100 50 0];
I_stack = timeseries(I, t);

t = [0 1500 3000];
T = [298 350 400];
T_stack = timeseries(T, t);
