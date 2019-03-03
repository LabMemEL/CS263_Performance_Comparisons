require 'gmp'
require 'benchmark'
require 'get_process_mem'
def matmul(a, b)
	m = a.length
	n = a[0].length
	p = b[0].length
	# transpose
	b2 = Array.new(n) { Array.new(p) { 0 } }
	for i in 0 .. n-1
		for j in 0 .. p-1
			b2[j][i] = b[i][j]
		end
	end
	# multiplication
  	c = Array.new(m) { Array.new(p) { 0 } }
	for i in 0 .. m-1
		for j in 0 .. p-1
			s = 0
			ai, b2j = a[i], b2[j]
			for k in 0 .. n-1
				s += ai[k] * b2j[k]
			end
			c[i][j] = s
		end
	end
	return c
end

def matgen(n)
	tmp = 1.0 / n / n
  	a = Array.new(n) { Array.new(n) { 0 } }
	for i in 0 .. n-1
		for j in 0 .. n-1
			a[i][j] = tmp * (i - j) * (i + j)
		end
	end
	return a
end

def test(x)
	n = (x||100).to_i
	# if ARGV.length >= 1
	# 	n = ARGV[0].to_i
	# end
	n = n / 2 * 2
	a = matgen(n)
	b = matgen(n)
	c = matmul(a, b)
	puts c[n/2][n/2]
end

# cpu and wall time
Benchmark.bm do |x|
	x.report('Times: ')        { test(1000) }
	# x.compare!
  end
  
  mem = GetProcessMem.new
  puts mem.inspect