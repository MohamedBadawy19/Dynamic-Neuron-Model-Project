import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, BarChart, Bar, PieChart, Pie, Cell, ScatterPlot, Scatter, ComposedChart, Area, AreaChart } from 'recharts';
import { Activity, Brain, Zap, TrendingUp, Clock, Target, BarChart3, Cpu } from 'lucide-react';

const PINNAnalysisDashboard = () => {
  const [activeTab, setActiveTab] = useState('overview');

  // Data from your analysis
  const trainingData = [
    { epoch: 0, totalLoss: 5.17e5, physicsLoss: 4.52e2, icLoss: 1.80e3, dataLoss: 3.12e3 },
    { epoch: 2000, totalLoss: 1.09e4, physicsLoss: 4.28e1, icLoss: 2.81e-2, dataLoss: 2.17e2 },
    { epoch: 4000, totalLoss: 5.74e3, physicsLoss: 4.70e1, icLoss: 1.37e-3, dataLoss: 1.14e2 },
    { epoch: 6000, totalLoss: 3.53e3, physicsLoss: 5.22e1, icLoss: 3.49e-4, dataLoss: 6.95e1 }
  ];

  const accuracyMetrics = [
    { metric: 'MAE', voltage: 0.156, recovery: 0.234 },
    { metric: 'RMSE', voltage: 0.203, recovery: 0.298 },
    { metric: 'Max Error', voltage: 1.245, recovery: 1.876 },
    { metric: 'Physics Residual', voltage: 0.0234, recovery: 0.0187 }
  ];

  const architectureData = [
    { layer: 'Input', neurons: 1, parameters: 0 },
    { layer: 'Hidden 1', neurons: 128, parameters: 256 },
    { layer: 'Hidden 2', neurons: 128, parameters: 16384 },
    { layer: 'Hidden 3', neurons: 128, parameters: 16384 },
    { layer: 'Hidden 4', neurons: 128, parameters: 16384 },
    { layer: 'Output', neurons: 2, parameters: 258 }
  ];

  const lossContribution = [
    { name: 'Physics Loss', value: 52.2, color: '#8884d8', percentage: 45.1 },
    { name: 'IC Loss (×200)', value: 0.0698, color: '#82ca9d', percentage: 12.3 },
    { name: 'Data Loss (×50)', value: 347.5, color: '#ffc658', percentage: 42.6 }
  ];

  const neuronalBehavior = [
    { time: 0, voltage: -70, recovery: 0.2, phase: 'Resting' },
    { time: 50, voltage: -68, recovery: 0.21, phase: 'Resting' },
    { time: 100, voltage: -65, recovery: 0.25, phase: 'Threshold' },
    { time: 105, voltage: 30, recovery: 0.8, phase: 'Spike' },
    { time: 110, voltage: -75, recovery: 0.9, phase: 'Recovery' },
    { time: 150, voltage: -70, recovery: 0.3, phase: 'Adapted' }
  ];

  const performanceMetrics = [
    { metric: 'Training Time', value: 1252.9, unit: 'seconds' },
    { metric: 'Inference Time', value: 12.5, unit: 'ms' },
    { metric: 'Parameters', value: 49666, unit: 'count' },
    { metric: 'Convergence Rate', value: 146, unit: '×' }
  ];

  const spikeAnalysis = [
    { parameter: 'Reference Spikes', value: 8 },
    { parameter: 'PINN Spikes', value: 8 },
    { parameter: 'Timing Error', value: 0.3 },
    { parameter: 'ISI Reference', value: 45.2 },
    { parameter: 'ISI PINN', value: 44.8 }
  ];

  const TabButton = ({ id, label, icon: Icon, active, onClick }) => (
    <button
      onClick={() => onClick(id)}
      className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
        active 
          ? 'bg-blue-600 text-white shadow-lg' 
          : 'bg-gray-100 hover:bg-gray-200 text-gray-700'
      }`}
    >
      <Icon size={18} />
      {label}
    </button>
  );

  const MetricCard = ({ title, value, unit, icon: Icon, color = 'blue' }) => (
    <div className={`bg-white rounded-xl p-6 shadow-lg border-l-4 border-${color}-500`}>
      <div className="flex items-center justify-between">
        <div>
          <p className="text-gray-600 text-sm font-medium">{title}</p>
          <p className="text-2xl font-bold text-gray-900">{value} <span className="text-sm text-gray-500">{unit}</span></p>
        </div>
        <Icon className={`text-${color}-500`} size={24} />
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-2xl shadow-xl p-8 mb-8">
          <div className="flex items-center gap-4 mb-4">
            <Brain className="text-blue-600" size={40} />
            <div>
              <h1 className="text-3xl font-bold text-gray-900">PINN Analysis Dashboard</h1>
              <p className="text-gray-600">Dynamic Neuron Model (Izhikevich) - Physics-Informed Neural Network</p>
            </div>
          </div>
          
          {/* Tab Navigation */}
          <div className="flex flex-wrap gap-3">
            <TabButton id="overview" label="Overview" icon={BarChart3} active={activeTab === 'overview'} onClick={setActiveTab} />
            <TabButton id="training" label="Training" icon={TrendingUp} active={activeTab === 'training'} onClick={setActiveTab} />
            <TabButton id="accuracy" label="Accuracy" icon={Target} active={activeTab === 'accuracy'} onClick={setActiveTab} />
            <TabButton id="neuronal" label="Neuronal" icon={Activity} active={activeTab === 'neuronal'} onClick={setActiveTab} />
            <TabButton id="performance" label="Performance" icon={Cpu} active={activeTab === 'performance'} onClick={setActiveTab} />
          </div>
        </div>

        {/* Overview Tab */}
        {activeTab === 'overview' && (
          <div className="space-y-8">
            {/* Key Metrics */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <MetricCard title="Total Parameters" value="49,666" unit="" icon={Cpu} color="purple" />
              <MetricCard title="Training Time" value="1253" unit="sec" icon={Clock} color="green" />
              <MetricCard title="PINN Spikes" value="8" unit="" icon={Zap} color="yellow" />
              <MetricCard title="Voltage MAE" value="0.156" unit="mV" icon={Activity} color="red" />
            </div>

            {/* Architecture Visualization */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                <Brain size={24} className="text-blue-600" />
                Neural Network Architecture
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={architectureData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="layer" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="neurons" fill="#8884d8" name="Neurons" />
                  <Bar dataKey="parameters" fill="#82ca9d" name="Parameters" />
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Loss Contribution Pie Chart */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4">Loss Component Contributions</h3>
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <ResponsiveContainer width="100%" height={300}>
                  <PieChart>
                    <Pie
                      data={lossContribution}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      label={({ name, percentage }) => `${name}: ${percentage}%`}
                      outerRadius={80}
                      fill="#8884d8"
                      dataKey="percentage"
                    >
                      {lossContribution.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={entry.color} />
                      ))}
                    </Pie>
                    <Tooltip />
                  </PieChart>
                </ResponsiveContainer>
                <div className="space-y-4">
                  {lossContribution.map((item, index) => (
                    <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                      <div className="flex items-center gap-3">
                        <div className={`w-4 h-4 rounded`} style={{backgroundColor: item.color}}></div>
                        <span className="font-medium">{item.name}</span>
                      </div>
                      <span className="text-sm text-gray-600">{item.percentage}%</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Training Tab */}
        {activeTab === 'training' && (
          <div className="space-y-8">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                <TrendingUp size={24} className="text-green-600" />
                Training Convergence
              </h3>
              <ResponsiveContainer width="100%" height={400}>
                <LineChart data={trainingData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="epoch" />
                  <YAxis scale="log" domain={[1, 1000000]} />
                  <Tooltip formatter={(value) => value.toExponential(2)} />
                  <Legend />
                  <Line type="monotone" dataKey="totalLoss" stroke="#8884d8" strokeWidth={3} name="Total Loss" />
                  <Line type="monotone" dataKey="physicsLoss" stroke="#82ca9d" strokeWidth={2} name="Physics Loss" />
                  <Line type="monotone" dataKey="dataLoss" stroke="#ffc658" strokeWidth={2} name="Data Loss" />
                  <Line type="monotone" dataKey="icLoss" stroke="#ff7300" strokeWidth={2} name="IC Loss" />
                </LineChart>
              </ResponsiveContainer>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h4 className="text-lg font-bold mb-4">Training Statistics</h4>
                <div className="space-y-3">
                  <div className="flex justify-between">
                    <span>Adam Epochs:</span>
                    <span className="font-mono">8,000</span>
                  </div>
                  <div className="flex justify-between">
                    <span>LBFGS Iterations:</span>
                    <span className="font-mono">100</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Collocation Points:</span>
                    <span className="font-mono">2,000</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Loss Improvement:</span>
                    <span className="font-mono text-green-600">146×</span>
                  </div>
                </div>
              </div>

              <div className="bg-white rounded-xl shadow-lg p-6">
                <h4 className="text-lg font-bold mb-4">Final Loss Values</h4>
                <div className="space-y-3">
                  <div className="flex justify-between">
                    <span>Physics Loss:</span>
                    <span className="font-mono">5.22×10⁻²</span>
                  </div>
                  <div className="flex justify-between">
                    <span>IC Loss:</span>
                    <span className="font-mono">3.49×10⁻⁴</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Data Loss:</span>
                    <span className="font-mono">6.95×10¹</span>
                  </div>
                  <div className="flex justify-between font-bold border-t pt-2">
                    <span>Total:</span>
                    <span className="font-mono">3.53×10³</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Accuracy Tab */}
        {activeTab === 'accuracy' && (
          <div className="space-y-8">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                <Target size={24} className="text-red-600" />
                Accuracy Metrics Comparison
              </h3>
              <ResponsiveContainer width="100%" height={350}>
                <BarChart data={accuracyMetrics}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="metric" />
                  <YAxis />
                  <Tooltip formatter={(value) => value.toFixed(4)} />
                  <Legend />
                  <Bar dataKey="voltage" fill="#8884d8" name="Voltage (mV)" />
                  <Bar dataKey="recovery" fill="#82ca9d" name="Recovery Variable" />
                </BarChart>
              </ResponsiveContainer>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h4 className="text-lg font-bold mb-4 text-blue-600">Voltage Accuracy</h4>
                <div className="space-y-4">
                  <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                    <span>MAE:</span>
                    <span className="font-mono font-bold">0.156 mV</span>
                  </div>
                  <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                    <span>RMSE:</span>
                    <span className="font-mono font-bold">0.203 mV</span>
                  </div>
                  <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                    <span>Max Error:</span>
                    <span className="font-mono font-bold">1.245 mV</span>
                  </div>
                  <div className="flex justify-between items-center p-3 bg-green-100 rounded-lg">
                    <span>Normalized Error:</span>
                    <span className="font-mono font-bold text-green-600">1.56%</span>
                  </div>
                </div>
              </div>

              <div className="bg-white rounded-xl shadow-lg p-6">
                <h4 className="text-lg font-bold mb-4 text-green-600">Recovery Variable Accuracy</h4>
                <div className="space-y-4">
                  <div className="flex justify-between items-center p-3 bg-green-50 rounded-lg">
                    <span>MAE:</span>
                    <span className="font-mono font-bold">0.234</span>
                  </div>
                  <div className="flex justify-between items-center p-3 bg-green-50 rounded-lg">
                    <span>RMSE:</span>
                    <span className="font-mono font-bold">0.298</span>
                  </div>
                  <div className="flex justify-between items-center p-3 bg-green-50 rounded-lg">
                    <span>Max Error:</span>
                    <span className="font-mono font-bold">1.876</span>
                  </div>
                  <div className="flex justify-between items-center p-3 bg-green-100 rounded-lg">
                    <span>Normalized Error:</span>
                    <span className="font-mono font-bold text-green-600">2.34%</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Neuronal Tab */}
        {activeTab === 'neuronal' && (
          <div className="space-y-8">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                <Activity size={24} className="text-purple-600" />
                Neuronal Dynamics Phase Space
              </h3>
              <ResponsiveContainer width="100%" height={400}>
                <LineChart data={neuronalBehavior}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="time" />
                  <YAxis yAxisId="left" />
                  <YAxis yAxisId="right" orientation="right" />
                  <Tooltip />
                  <Legend />
                  <Line yAxisId="left" type="monotone" dataKey="voltage" stroke="#8884d8" strokeWidth={3} name="Voltage (mV)" />
                  <Line yAxisId="right" type="monotone" dataKey="recovery" stroke="#82ca9d" strokeWidth={2} name="Recovery Variable" />
                </LineChart>
              </ResponsiveContainer>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h4 className="text-lg font-bold mb-4 flex items-center gap-2">
                  <Zap size={20} className="text-yellow-600" />
                  Spike Analysis
                </h4>
                <div className="space-y-3">
                  {spikeAnalysis.map((item, index) => (
                    <div key={index} className="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
                      <span className="text-sm font-medium">{item.parameter}:</span>
                      <span className="font-mono font-bold">{item.value}</span>
                    </div>
                  ))}
                </div>
              </div>

              <div className="bg-white rounded-xl shadow-lg p-6">
                <h4 className="text-lg font-bold mb-4">Neuronal Properties</h4>
                <div className="space-y-4">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <div className="flex justify-between items-center">
                      <span className="font-medium">Resting Potential:</span>
                      <span className="text-xl font-bold text-blue-600">-70.0 mV</span>
                    </div>
                  </div>
                  <div className="p-4 bg-red-50 rounded-lg">
                    <div className="flex justify-between items-center">
                      <span className="font-medium">Peak Potential:</span>
                      <span className="text-xl font-bold text-red-600">+30.0 mV</span>
                    </div>
                  </div>
                  <div className="p-4 bg-green-50 rounded-lg">
                    <div className="flex justify-between items-center">
                      <span className="font-medium">AP Amplitude:</span>
                      <span className="text-xl font-bold text-green-600">100.0 mV</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Performance Tab */}
        {activeTab === 'performance' && (
          <div className="space-y-8">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {performanceMetrics.map((metric, index) => (
                <MetricCard 
                  key={index}
                  title={metric.metric} 
                  value={metric.value.toLocaleString()} 
                  unit={metric.unit} 
                  icon={Cpu} 
                  color="indigo" 
                />
              ))}
            </div>

            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                <Clock size={24} className="text-indigo-600" />
                Computational Efficiency
              </h3>
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <div>
                  <h4 className="text-lg font-semibold mb-4">Training Performance</h4>
                  <div className="space-y-3">
                    <div className="flex justify-between p-3 bg-indigo-50 rounded-lg">
                      <span>Total Training Time:</span>
                      <span className="font-mono font-bold">1,252.9 sec</span>
                    </div>
                    <div className="flex justify-between p-3 bg-indigo-50 rounded-lg">
                      <span>Time per Epoch:</span>
                      <span className="font-mono font-bold">0.157 sec</span>
                    </div>
                    <div className="flex justify-between p-3 bg-indigo-50 rounded-lg">
                      <span>Parameters/Second:</span>
                      <span className="font-mono font-bold">39.6</span>
                    </div>
                  </div>
                </div>
                <div>
                  <h4 className="text-lg font-semibold mb-4">Inference Performance</h4>
                  <div className="space-y-3">
                    <div className="flex justify-between p-3 bg-green-50 rounded-lg">
                      <span>Inference Time (1000 pts):</span>
                      <span className="font-mono font-bold">12.5 ms</span>
                    </div>
                    <div className="flex justify-between p-3 bg-green-50 rounded-lg">
                      <span>Inference Speed:</span>
                      <span className="font-mono font-bold">80,000 pts/sec</span>
                    </div>
                    <div className="flex justify-between p-3 bg-green-50 rounded-lg">
                      <span>Memory Usage:</span>
                      <span className="font-mono font-bold">~194 KB</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-white rounded-xl shadow-lg p-6">
              <h4 className="text-lg font-bold mb-4">PINN Method Advantages</h4>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {[
                  "Mesh-free solution (continuous in time)",
                  "Automatic differentiation for physics laws",
                  "Handles irregular/sparse data naturally",
                  "Incorporates prior physics knowledge",
                  "Provides smooth interpolation everywhere",
                  "Can handle inverse problems easily",
                  "Biomedically relevant for neural prosthetics",
                  "Suitable for real-time applications"
                ].map((advantage, index) => (
                  <div key={index} className="flex items-center gap-3 p-3 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg">
                    <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                    <span className="text-sm">{advantage}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Footer */}
        <div className="bg-white rounded-xl shadow-lg p-6 mt-8">
          <div className="text-center">
            <h3 className="text-lg font-bold text-gray-800 mb-2">Complete Analysis for Numerical Methods Project</h3>
            <p className="text-gray-600">Physics-Informed Neural Network successfully models Izhikevich neuron dynamics with high accuracy</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PINNAnalysisDashboard;