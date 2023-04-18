<script>
	import '../app.css';

	let listaOpciones = [
		{ id: '1', nombre: 'Alienígena' },
		{ id: '2', nombre: 'Fan de Cristiano Ronaldo' },
		{ id: '3', nombre: 'Poeta del siglo XVIII' },
		{ id: '4', nombre: 'Científico loco' }
	];
	let opcionSeleccionada = listaOpciones[0].id;
	let prompt = '';

	async function sendPromt() {
		let formData = new FormData();
		formData.append('prompt', prompt);
		formData.append('preprompt', opcionSeleccionada);

		fetch('https://abrahammh99.pythonanywhere.com/api/v1/open_ai_respuesta', {
			method: 'POST',
			body: formData
		})
			.then((response) => response.json())
			.then((data) => {
				console.log(data);
			})
			.catch((error) => {
				console.error('Error:', error);
			});
	}
</script>

<div class="container mx-auto mt-20 px-5 md:px-20 lg:px-96">
	<div class="flex justify-center text-white font-bold text-5xl">OpenAI API test</div>
	<div class="my-24">
		<p class="text-lg mb-5">
			<span class="kbd mr-3">1</span>
			Escribe tu prompt.
		</p>
		<textarea
			bind:value={prompt}
			class="mb-8 w-full h-36 text-lg py-2 px-4 rounded-lg bg-base-200 border-2 border-base-300 focus:border-emerald-500 focus:outline-none"
			placeholder="Escribe aquí..."
		/>
		<p class="text-lg mb-5">
			<span class="kbd mr-3">2</span>
			Selecciona la forma en la que se responderá.
		</p>
		<select
			bind:value={opcionSeleccionada}
			class="mb-10 select w-full text-lg bg-base-200 border-2 border-base-300 focus:outline-none focus:border-emerald-500"
		>
			{#each listaOpciones as opcion}
				<option value={opcion.id}>{opcion.nombre}</option>
			{/each}
		</select>
		<button on:click={sendPromt} class="btn btn-success w-full">Generar respuesta</button>
	</div>
</div>
