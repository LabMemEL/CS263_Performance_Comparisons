require 'gmp'
require 'benchmark'
require 'get_process_mem'
# require_relative '../../posixpsutil/lib/posixpsutil'
# CPU = PosixPsutil::CPU
# def show_cpu()
#   puts "The CPU number is #{CPU.cpu_count}"
#   puts "The physical CPU number is #{CPU.cpu_count(false)}"
#   puts "Total CPU times: #{CPU.cpu_times}"
#   puts "Each CPU times: #{CPU.cpu_times(true)}"
#   sleep 1
#   puts "The CPU percent(immediate) : #{CPU.cpu_percent(0.1)}"
#   puts "The CPU percent(after a second) : #{CPU.cpu_percent(1.0)}"
#   puts "Each CPU percent(immediate) : #{CPU.cpu_percent(0.1, true)}"
#   puts "Each CPU percent(after a second) : #{CPU.cpu_percent(1.0, true)}"
#   puts "Each CPU percent(immediate) : #{CPU.cpu_times_percent(0.1, true)}"
#   puts "Each CPU percent(after a second) : #{CPU.cpu_times_percent(1.0, true)}"
# end






# Helpers that improve readability
class GMP::Z
  def mul!(a,b)
    GMP::Z.mul(self, a, b)
  end

  def times!(a)
    GMP::Z.mul(self, self, a)
  end
end

# Constants to reduce object instantiation and casting
ZERO = GMP::Z(0)
ONE = GMP::Z(1)
TWO = GMP::Z(2)
THREE = GMP::Z(3)
TEN = GMP::Z(10)

# Allocate these expensive objects once
@display_chunk = GMP::Z(0)
@k = GMP::Z(0)
@a = GMP::Z(0)
@t = GMP::Z(0)
@u = GMP::Z(0)
@k1 = GMP::Z(1)
@n = GMP::Z(1)
@d = GMP::Z(1)
@tmp = GMP::Z(0)

def next_chunk
  @tmp.mul!(@d, @t)
  @a.sub!(@tmp)
  @a.times!(TEN)
  @n.times!(TEN)
end

def produce_chunk
  @k.add!(ONE)
  @t.mul!(@n, TWO)
  @n.times!(@k)

  @a.add!(@t)
  @k1.add!(TWO)
  @a.times!(@k1)
  @d.times!(@k1)

  if @a >= @n
    @tmp.mul!(@n, THREE)
    @tmp.add!(@a)
    @t = @tmp.fdiv(@d)
    @u = @tmp.fmod(@d)
    @u.add!(@n)
    if @d > @u
      @display_chunk.times!(TEN)
      @display_chunk.add!(@t)
      return true
    end
  end

  false
end

def test(n)
  range = (n || 100).to_i
  count = 0
  while(count < range) do
    if produce_chunk
      count += 1
      if count % 10 == 0
        STDOUT.write "%010d\t:%d\n" % [@display_chunk.to_i, count]
        @display_chunk.times!(ZERO)
      end
      next_chunk
    end
  end
  if @display_chunk.to_i > 0
    STDOUT.write "%s\t:%d\n" % [@display_chunk.to_s.ljust(10), count]
  end
  STDOUT.write '*'*50+"\n"
end



# puts "Start running the CPU example"
# show_cpu()
# puts ""




# cpu and wall time
Benchmark.bm do |x|
  x.report('Times: ')        { test(10000) }
  # x.compare!
end

mem = GetProcessMem.new
puts mem.inspect
