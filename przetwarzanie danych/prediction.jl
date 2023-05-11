##
using StatsKit, Dates, Interpolations
using Plots, StatsPlots

##
dataset = CSV.read("C:\\Users\\kkarb\\OneDrive\\Pulpit\\projektpm\\SSHprojekt\\klucze\\ppm\\data\\2016-2022.csv", select = [:year,:event_date,:event_type, :sub_event_type, :interaction, :admin1, :location, :latitude, :longitude, :fatalities], DataFrame)

##
function timeseries_gen(df::DataFrame, region::String, years::Tuple{Int,Int}, event_type::String = "any", fill::Bool=true, log_scale::Bool=false)
	data = select(df, [:year, :event_date, :admin1, :event_type])
	data = subset(data, :year => y -> y .> years[1]-1 .&& y .< years[2]+1, :admin1 => a -> a .== region)
	if event_type != "any"
		data = subset(data, :event_type => e -> e .== event_type)
	end
	data[!, :time_stamp] = Date.(data.event_date, "d U y")
	count = sort(countmap(data[!,:time_stamp]))
	t = Dates.value.([keys(count)...].-Date(years[1],1,1))
	n = [values(count)...]
	if fill
		l = Int(Dates.value(Date(years[2]+1,1,1)-Day(1)-Date(years[1],1,1)))
		for i in 1:l+1
			try
				if t[i] != i-1
					insert!(t,i,i-1)
					insert!(n,i,0)
					
				end
			catch e
				if isa(e, BoundsError)
					insert!(t,i,i-1)
					insert!(n,i,0)
				else
					throw(e)
				end
			end
		end
	end
	if log_scale
		n = [val == 0 ? 0 : log(val) for val in n]
	end
	ts    = DataFrame(t = t, n = n)
end
years = 2016,2018
city = "Jammu and Kashmir"
flog = false
ts = timeseries_gen(dataset, city, years, "Protests", true,flog)
ts |> @df plot(:t,:n,dpi=600,title=city*" in $(years[1])-$(years[end])",xlabel="t [day]",ylabel="number of events",legend=false)


d = ts |> @df plot(:t,:n,xlabel="t [day]",ylabel="number of events",label="",dpi=600)
##
loenp = []
tp = range(extrema(ts.t)...; step = .1);
for i in [0.02,0.1,0.15,0.25]
	model = loess(ts.t, ts.n, span=i);
	np = Loess.predict(model, tp);
	push!(loenp,np)
	plot!(tp,np,palette=cgrad(:buda, 4, categorical = true),label="span=$(i)")
end
np = loenp[3]
display(d)

##
dif = ts.n .- [np[1:10:end]...]
plot(ts.t, dif, dpi=600)
histogram(dif, dpi=600, xlabel="number of events",ylabel="number of occurrences", legend=false)

##
timedata_fit = DataFrame(t = ts.t, n = np[1:10:end])
timedata_fit |> @df plot(:t,:n,dpi=600)

##
fi = fit_mle(Normal, dif)
StatsPlots.plot(fi, dpi=600)

##
fi2 = fit_mle(LogNormal, dif.+15)
StatsPlots.plot(fi2.-15, dpi=600)

##
acr_timedata = autocor(timedata_fit.n)
plot(acr_timedata[1:10])

##
acr_tsn = autocor(ts.n,demean=true)
plot(acr_tsn,minorgrid=true,dpi=600,title="Autocorrelation", xlabel="lag", ylabel="coefficient", legend=false)

##
acr_rand = autocov(rand(500))
plot(acr_rand[1:10])

##
d1 = timeseries_gen(dataset, city, years, "Strategic developments", true,flog)

##
cross = crosscor(d1.n,ts.n)
plot(cross)

##
#using NearestNeighbors
#function mean_prediction(df::DataFrame, n::Int64)
#	res = vcat(df.t',df.n')
#	l = length(df.t)
#	println(size(res))
#	for i = 1:n
#		tr = KDTree(res,Euclidean(),leafsize=5)
#		inds1, vals1 = knn(tr, [res[1,end]; res[2,end]],3,true)
#		inds2, vals2 = knn(tr, [res[1,end-1]; res[2,end-1]],3,true)
#		res = [res [l+i; mean([x for x in [vals1[2:end]..., vals2[2:end]...]])]]
#	end
#	res
#end

#predicted = mean_prediction(timedata_fit,100)
#t = predicted[1,:]
#n = predicted[2,:]
#plot(n)

#itp = interpolate(timedata_fit.n, BSpline(Quadratic(Periodic(OnCell()))))
#etp = extrapolate(itp, Periodic())
r = rand(fi,length(timedata_fit.t))
first(timeseries_gen(dataset, city, years.+2, "Protests", true,flog), 200) |> @df plot(:t,:n,dpi=600, label="Original data",title="Forecast for $(years[end]+1)",xlabel="t [day]",ylabel="number of events")
plot!((r+np[1:10:end])[1:200], linestyle=:dot, label="Normal distribution")
r = rand(fi2,length(timedata_fit.t))
plot!((r.-15+np[1:10:end])[1:200], linestyle=:dash, label="Log-normal distribution")

#using Optim

#using ARCHModels
#ARCHModels.ARCHLMTest(ts.n, 1)
#mod = ARCHModels.fit(GARCH{1, 1}, Float64.(ts.n))
#sim = ARCHModels.simulate(mod)
#am4 = ARCHModels.simulate(sim, 70)

#T = length(BG96);
#windowsize = 1000;
#vars = similar(BG96);
#for t = windowsize+1:T-1
#    m = fit(ARCH{1}, BG96[t-windowsize:t]);
#    vars[t+1] = predict(m, :VaR; level=0.05);
#end
#plot(1:1000,BG96[1:1000])
#plot!(1000:1974,vars[1000:end])

using StateSpaceModels

y = Vector{Float64}(ts.n)

model = auto_ets(y)

StateSpaceModels.fit!(model)

print_results(model)

forec = StateSpaceModels.forecast(model, 100)


plot(model, forec,dpi=600,title="Auto ETS", xlabel="time [day]", ylabel="number of events",labels=["original data" "prediction"])