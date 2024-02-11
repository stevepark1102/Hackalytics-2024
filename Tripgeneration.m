filename = 'Densitites.xlsx'
ca1 = readcell(filename);
%assumed coefficents based on resaonable assumptions 
base_val = 1.5;
popul_coeff = 0.0001;

population = input('Input Popualtion')
total_area_mi2 = input('Input total area in squre miles')
average_trips_per_person = base_val + popul_coeff*population

Tg = population*average_trips_per_person*serviceActualFactor

population_density = cell2mat(ca1(2:end, 2));
avg_population_density = mean(population_density) * 2.58999;

% Calculate population density per square mile
population_density_actual = population / avg_population_density;

estimated_zones = round((population / (population_density_actual * total_area_mi2)) * 1000);

% Optimization using fmincon for variable densities and trips generated
objective = @(x) -sum(x .* trips_generated(x, Tg)); % Objective: Minimize the negative of the sum of placements weighted by trips generated
A = []; b = []; Aeq = []; beq = [];
lb = zeros(estimated_zones, 1); % Lower bound for density in each zone
ub = ones(estimated_zones, 1) * 10; % Upper bound for density in each zone, adjust as needed
initial_guess = ones(estimated_zones, 1); % Initial guess

% Run optimization
density_per_zone = fmincon(objective, initial_guess, A, b, Aeq, beq, lb, ub);

% Display Results
disp('Optimal Density Per Zone:');
disp(density_per_zone(1));

% Function to calculate trips generated based on density and Tg
function trips = trips_generated(density, Tg)
    trips = density .* Tg;
end
