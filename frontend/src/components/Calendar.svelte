<script>
	const date = new Date();
	
	const today = {
		dayNumber: date.getDate(),
		month: date.getMonth(),
		year: date.getFullYear(),
	}
	
	const monthNames = [ "January1", "February2", "March3", "April4", "May5", "June6", "July7", "August8", "September9", "October10", "November11", "December12"];
	let monthIndex = date.getMonth();
	// const currentMonth = date.toLocaleString('en-US', { month: 'long' })
	$: month = monthNames[monthIndex];
	
	let year = date.getFullYear();
	
	$: firstDayIndex = new Date(year, monthIndex, 1).getDay();
	// const currentDay = date.getDate();
	$: numberOfDays = new Date(year, monthIndex+1, 0).getDate();
	
	$: calendarCellsQty = numberOfDays + firstDayIndex;
	
	const goToNextMonth = () => {
		if (monthIndex >= 11) {
			year += 1;
			return monthIndex = 0;
		}
		return monthIndex += 1;
	}
	
	const goToPrevMonth = () => {
		if (monthIndex <= 0) {
			year -= 1;
			return monthIndex = 11;
		}
		return monthIndex -= 1;
	}
	
	$: console.log(`${month}, ${today.dayNumber}, ${year}, FIRST DAY index is ${firstDayIndex}, MONTH index is ${monthIndex}, No. of days: ${numberOfDays}`)
</script>


	<div class="month">
		<ul>
			<li class="prev" >
				<button class="btn" on:click={goToPrevMonth}>&#10094;</button>
		    </li>
			<li class="next" >
				<button class="btn" on:click={goToNextMonth}>&#10095;</button>
			</li>
			
			<li>{month}<br>
				<span style="font-size:18px">{year}</span>
			</li>
		</ul>
	</div>

	<ul class="weekdays">
		<li>Su</li>
		<li>Mo</li>
		<li>Tu</li>
		<li>We</li>
		<li>Th</li>
		<li>Fr</li>
		<li>Sa</li>
	</ul>

	<ul class="days">
		{#each Array(calendarCellsQty) as _, i}
			{#if i < firstDayIndex || i >= numberOfDays+firstDayIndex  }
				<li>&nbsp;<br></li>
			{:else}
				<li class="{year.toString()}{
					(monthIndex + 1).toString().padStart(2,'0')}{((i - firstDayIndex) + 1).toString().padStart(2,'0')}" 
					class:active={i === today.dayNumber+(firstDayIndex-1) &&
					monthIndex === today.month &&
					year === today.year}>
					{(i - firstDayIndex) + 1}<br>
				</li>
			{/if}
		{/each}
	</ul>


				
<style>
	ul {list-style-type: none;}

	/* Month header */
	.month {
		/* padding: 70px 25px; */
		padding: 10px 3px;
		width: auto;
		background: #1abc9c;
		text-align: center;
	}

	/* Month list */
	.month ul {
		margin: 0;
		padding: 0;
	}

	.month ul li {
		color: white;
		font-size: 20px;
		text-transform: uppercase;
		letter-spacing: 3px;
	}

	/* Previous button inside month header */
	.month .prev {
		float: left;
		padding-top: 10px;
		cursor: pointer;
	}

	/* Next button */
	.month .next {
		float: right;
		padding-top: 10px;
		cursor: pointer;
	}

	/* Weekdays (Mon-Sun) */
	.weekdays {
		margin: 0;
		padding: 3px 0;
		background-color:#ddd;
	}

	.weekdays li {
		
		display: inline-block;
		/* width: 13.6%; */
		width: 13%;
		color: #666;
		text-align: center;
		font-size: 0.9rem;
	}

	/* Days (1-31) */
	.days {
		margin: 0;
		padding: 3px 0;
		/* padding: 10px 0; */
		background: #eee;

	}

	.days li {
		list-style-type: none;
		display: inline-block;
		border: 1px solid black;
		padding: 3px;
		margin: 1px;
		/* padding: 9px; */
		width: 13.6%;
		/* width: 11.6%; */
		text-align: center;
		/* margin-bottom: 1px; */
		font-size: 1.2rem;
		color: #777;
		cursor: pointer;
	}

	/* Highlight the "current" day */
	.active {
		padding: 5px;
		background: #1abc9c;
		color: white !important
	}
</style>