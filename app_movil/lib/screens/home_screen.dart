import 'package:app_movil/models/reparacion.dart';
import 'package:app_movil/providers/taller_provider.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import '../core/router.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final PageController _pageController = PageController();
  int _paginaActual = 0;
  String _filtroEstado = 'Todas';

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  void _cambiarPagina(int index) {
    setState(() => _paginaActual = index);
    _pageController.animateToPage(
      index,
      duration: const Duration(milliseconds: 250),
      curve: Curves.easeInOut,
    );
  }

  void _mostrarDetalleReparacion(
    BuildContext context,
    Reparacion rep,
    TallerProvider provider,
  ) {
    showModalBottomSheet(
      context: context,
      showDragHandle: true,
      builder: (_) => Padding(
        padding: const EdgeInsets.fromLTRB(20, 0, 20, 24),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Expanded(
                  child: Text(
                    rep.equipo,
                    style: Theme.of(context).textTheme.titleLarge,
                  ),
                ),
                Chip(label: Text(rep.estado)),
              ],
            ),
            const SizedBox(height: 12),
            Text('Cliente: ${provider.obtenerNombreCliente(rep.cliente)}'),
            const SizedBox(height: 4),
            Text('Técnico: ${provider.obtenerNombreTecnico(rep.tecnico)}'),
            const SizedBox(height: 4),
            Text(
              'Coste: ${rep.coste.toStringAsFixed(2)} €',
              style: const TextStyle(fontWeight: FontWeight.bold),
            ),
            const Divider(height: 24),
            Text(
              'Descripción:',
              style: Theme.of(context).textTheme.labelLarge,
            ),
            const SizedBox(height: 4),
            Text(rep.descripcion),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final provider = context.watch<TallerProvider>();

    return Scaffold(
      appBar: AppBar(
        title: Text(provider.nombreTaller ?? 'Taller'),
        actions: [
          IconButton(
            tooltip: 'Actualizar datos',
            icon: const Icon(Icons.refresh),
            onPressed: provider.cargando ? null : () => provider.cargarDatos(),
          ),
          IconButton(
            tooltip: 'Cerrar sesión',
            icon: const Icon(Icons.logout),
            onPressed: () {
              provider.cerrarSesion();
              context.goNamed(MiRouter.login);
            },
          ),
        ],
      ),
      body: provider.cargando && provider.reparaciones.isEmpty
    ? const Center(child: CircularProgressIndicator())
    : provider.error != null
        ? Center(
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    'Error: ${provider.error}',
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 12),
                  FilledButton(
                    onPressed: () => provider.cargarDatos(),
                    child: const Text('Reintentar'),
                  ),
                ],
              ),
            ),
          )
        : PageView(
              controller: _pageController,
              onPageChanged: (index) => setState(() => _paginaActual = index),
              children: [
                _buildTabReparaciones(provider),
                _buildTabClientes(provider),
                _buildTabTecnicos(provider),
                _buildTabEstadisticas(provider),
              ],
            ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: _paginaActual,
        onDestinationSelected: _cambiarPagina,
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.build_outlined),
            selectedIcon: Icon(Icons.build),
            label: 'Reparaciones',
          ),
          NavigationDestination(
            icon: Icon(Icons.people_outline),
            selectedIcon: Icon(Icons.people),
            label: 'Clientes',
          ),
          NavigationDestination(
            icon: Icon(Icons.engineering_outlined),
            selectedIcon: Icon(Icons.engineering),
            label: 'Técnicos',
          ),
          NavigationDestination(
            icon: Icon(Icons.bar_chart_outlined),
            selectedIcon: Icon(Icons.bar_chart),
            label: 'Resumen',
          ),
        ],
      ),
    );
  }

  Widget _buildTabReparaciones(TallerProvider provider) {
    const estados = ['Todas', 'Pendiente', 'En proceso', 'Finalizada'];
    final filtradas = _filtroEstado == 'Todas'
        ? provider.reparaciones
        : provider.reparaciones
            .where((r) => r.estado.toLowerCase() == _filtroEstado.toLowerCase())
            .toList();

    return Column(
      children: [
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
          child: Row(
            children: estados.map((estado) {
              return Padding(
                padding: const EdgeInsets.only(right: 8),
                child: ChoiceChip(
                  label: Text(estado),
                  selected: _filtroEstado == estado,
                  onSelected: (_) => setState(() => _filtroEstado = estado),
                ),
              );
            }).toList(),
          ),
        ),
        Expanded(
          child: RefreshIndicator(
            onRefresh: provider.cargarDatos,
            child: filtradas.isEmpty
                ? ListView(
                    children: const [
                      SizedBox(height: 120),
                      Center(child: Text('No hay reparaciones que mostrar')),
                    ],
                  )
                : ListView.builder(
                    padding: const EdgeInsets.only(bottom: 16),
                    itemCount: filtradas.length,
                    itemBuilder: (context, index) {
                      final rep = filtradas[index];
                      return Card(
                        margin: const EdgeInsets.symmetric(
                          horizontal: 12,
                          vertical: 6,
                        ),
                        child: InkWell(
                          borderRadius: BorderRadius.circular(12),
                          onTap: () =>
                              _mostrarDetalleReparacion(context, rep, provider),
                          child: Padding(
                            padding: const EdgeInsets.all(12),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  children: [
                                    Expanded(
                                      child: Text(
                                        rep.equipo,
                                        style: Theme.of(context)
                                            .textTheme
                                            .titleMedium,
                                        maxLines: 1,
                                        overflow: TextOverflow.ellipsis,
                                      ),
                                    ),
                                    const SizedBox(width: 8),
                                    Chip(
                                      label: Text(rep.estado),
                                      visualDensity: VisualDensity.compact,
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 4),
                                Text(
                                  rep.descripcion,
                                  maxLines: 2,
                                  overflow: TextOverflow.ellipsis,
                                ),
                                const Divider(height: 16),
                                Row(
                                  mainAxisAlignment:
                                      MainAxisAlignment.spaceBetween,
                                  children: [
                                    Expanded(
                                      child: Text(
                                        provider
                                            .obtenerNombreCliente(rep.cliente),
                                        overflow: TextOverflow.ellipsis,
                                      ),
                                    ),
                                    Text(
                                      '${rep.coste.toStringAsFixed(2)} €',
                                      style: const TextStyle(
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                          ),
                        ),
                      );
                    },
                  ),
          ),
        ),
      ],
    );
  }

  Widget _buildTabClientes(TallerProvider provider) {
    final clientes = provider.clientes.values.toList();

    return RefreshIndicator(
      onRefresh: provider.cargarDatos,
      child: clientes.isEmpty
          ? ListView(
              children: const [
                SizedBox(height: 120),
                Center(child: Text('No hay clientes registrados')),
              ],
            )
          : ListView.builder(
              padding: const EdgeInsets.symmetric(vertical: 8),
              itemCount: clientes.length,
              itemBuilder: (_, index) {
                final c = clientes[index];
                return Card(
                  margin:
                      const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
                  child: ListTile(
                    leading: CircleAvatar(
                      child: Text(
                        c.nombre.isNotEmpty ? c.nombre[0].toUpperCase() : '?',
                      ),
                    ),
                    title: Text(c.nombre),
                    subtitle: Text(
                      [
                        if (c.numero.isNotEmpty) c.numero,
                        if (c.email.isNotEmpty) c.email,
                      ].join(' · '),
                    ),
                  ),
                );
              },
            ),
    );
  }

  Widget _buildTabTecnicos(TallerProvider provider) {
    final tecnicos = provider.tecnicos.values.toList();

    return RefreshIndicator(
      onRefresh: provider.cargarDatos,
      child: tecnicos.isEmpty
          ? ListView(
              children: const [
                SizedBox(height: 120),
                Center(child: Text('No hay técnicos registrados')),
              ],
            )
          : ListView.builder(
              padding: const EdgeInsets.symmetric(vertical: 8),
              itemCount: tecnicos.length,
              itemBuilder: (_, index) {
                final t = tecnicos[index];
                return Card(
                  margin:
                      const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
                  child: ListTile(
                    leading: const CircleAvatar(child: Icon(Icons.engineering)),
                    title: Text(t.nombre),
                    subtitle: Text('Especialidad: ${t.especialidad}'),
                  ),
                );
              },
            ),
    );
  }

  Widget _buildTabEstadisticas(TallerProvider provider) {
    return RefreshIndicator(
      onRefresh: provider.cargarDatos,
      child: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          _tarjetaMetrica(
            context,
            titulo: 'Ingresos totales',
            valor: '${provider.ingresosTotales.toStringAsFixed(2)} €',
            icono: Icons.euro,
          ),
          const SizedBox(height: 12),
          Row(
            children: [
              Expanded(
                child: _tarjetaMetrica(
                  context,
                  titulo: 'Clientes',
                  valor: '${provider.clientes.length}',
                  icono: Icons.people,
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: _tarjetaMetrica(
                  context,
                  titulo: 'Técnicos',
                  valor: '${provider.tecnicos.length}',
                  icono: Icons.engineering,
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Reparaciones (${provider.reparaciones.length})',
                    style: Theme.of(context).textTheme.titleMedium,
                  ),
                  const Divider(height: 20),
                  _filaEstado('Pendientes', provider.contarPorEstado('Pendiente')),
                  const SizedBox(height: 8),
                  _filaEstado('En proceso', provider.contarPorEstado('En proceso')),
                  const SizedBox(height: 8),
                  _filaEstado('Finalizadas', provider.contarPorEstado('Finalizada')),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _tarjetaMetrica(
    BuildContext context, {
    required String titulo,
    required String valor,
    required IconData icono,
  }) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(
          children: [
            Icon(icono, size: 32),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(titulo, style: Theme.of(context).textTheme.labelLarge),
                  const SizedBox(height: 4),
                  Text(valor, style: Theme.of(context).textTheme.headlineSmall),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _filaEstado(String etiqueta, int cantidad) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(etiqueta),
        Text(
          '$cantidad',
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
      ],
    );
  }
}