<script>
	import fastapi from "../../lib/api";
	import Modal2 from '../../components/Modal2.svelte';
	import Info from "./Info.svelte";
	const date = new Date();
  
	const today = {
	  dayNumber: date.getDate(),
	  month: date.getMonth(),
	  year: date.getFullYear(),
	}
	  
	const monthNames = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
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
		// console.log(year)
	  //   search_worked(year, 0)
		  return monthIndex = 0;
	  }
		// console.log(year)
	  //   search_worked(year, monthIndex+1)
		return monthIndex += 1;
	}
	  
	const goToPrevMonth = () => {
	  if (monthIndex <= 0) {
		year -= 1;
		// console.log(year)
	  //   search_worked(year, 11)
		return monthIndex = 11;
	  }
		// console.log(year)
	  //   search_worked(year, monthIndex-1)
		return monthIndex -= 1;
	}
  
  
  
	let worked_list = []
  let workedDayInfo = []
	let workedDays = []
	let workedPlaces = []
	let workedPlacesSelect = workedPlaces
	
	function search_worked(year, monthIndex) {
	  //   console.log(year)
	  //   console.log(monthIndex+1)
	  let params = {
		year: year,
		month: monthIndex+1,
	  }
	  fastapi('get', '/api/worked/list', params, (json) => {
		worked_list = json.worked_list
		workedDays = [] 
		workedPlaces = []
    workedDayInfo = []
		for (let i = 0; i < worked_list.length; i++) {
		  let workedDay = (worked_list[i].year*10000 + worked_list[i].month*100 + worked_list[i].day).toString()
		  workedDays.push(workedDay)
		  workedDayInfo.push(workedDay)
		  // console.log(worked_list[i].note)
		  if (!workedPlaces.includes(worked_list[i].note)) {
			  workedPlaces.push(worked_list[i].note)
		  }
		}
    console.log(workedDays)
	  console.log(worked_list)
	  })
	}
	function getWorkedDays(workedPlacesSelect) {
	  workedDays = []
	  for (let i = 0; i < worked_list.length; i++) {
		  console.log(worked_list[i])
      // let workedDay = (worked_list[i].year*10000 + worked_list[i].month*100 + worked_list[i].day).toString()
		  // workedDays.push(workedDay)
		  if (workedPlacesSelect.includes(worked_list[i].note)){
		    let workedDay = (worked_list[i].year*10000 + worked_list[i].month*100 + worked_list[i].day).toString()
		    workedDays.push(workedDay)
		  }
	  }
    console.log(workedDays)
	}
	$: getWorkedDays(workedPlacesSelect), workedPlacesSelect
	$: search_worked(year, monthIndex)
	
	function get_NoteWage(year, month, day) {
	  let params = {
		year: year,
		month: month,
		day: day
	  }
	  fastapi('get', '/api/worked/detail', params, (json) => {
      console.log(json)
      noteInfo = json.note
      wageInfo = json.wage
      //   return json.note
      // console.log(typeof(noteInfo))
		}
	  )
	}
  
	function get_keywords() {
	  fastapi('get', '/api/worked/keywords', {}, (json) => {
		  // console.log(json)
		  keywords = json.keywords
		  // console.log(keywords)
		  return keywords
		}
	  )
	}
  
	let yearInfo
	let monthInfo
	let dayInfo
	let noteInfo 
	let wageInfo 
  //   let note
	let keywords = []
	function exportInfoData(year, month, day) {
	  // get_keywords()  
	  get_NoteWage(year, month, day)
	  get_keywords()
  
	  yearInfo = year
	  monthInfo = month
	  dayInfo = day
	  console.log(yearInfo, monthInfo, dayInfo, noteInfo, wageInfo, keywords)
	  // console.log(day)
	  // console.log(worked)
	  // get_noteInfo(yearInfo, monthInfo, dayInfo)
	  //   noteInfo = get_note(yearInfo, monthInfo, dayInfo)
	  //   get_worked(yearInfo, monthInfo, dayInfo)
	  //   noteInfo
	}
  
	  // $: console.log(`${month}, ${today.dayNumber}, ${year}, FIRST DAY index is ${firstDayIndex}, MONTH index is ${monthIndex}, No. of days: ${numberOfDays}`)
  </script>
  
  
  
  <Modal2>
	<Info {yearInfo} {monthInfo} {dayInfo} {noteInfo} {keywords} {wageInfo} {workedDayInfo}/>
	 <!-- {noteInfo} {keywords}/> -->
  </Modal2>
  
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
  
  <div class="row weekdays">
	<div class=col>Su</div>
	<div class=col>Mo</div>
	<div class=col>Tu</div>
	<div class=col>We</div>
	<div class=col>Th</div>
	<div class=col>Fr</div>
	<div class=col>Sa</div>
  </div>
  
  <div class="row days">
	{#each Array(calendarCellsQty) as _, i}
	{#if i < firstDayIndex || i >= numberOfDays+firstDayIndex  }
	  <li>&nbsp;<br></li>
	{:else}
	  <li class:worked={
			workedDays.includes((year*10000 + (monthIndex + 1)*100 + ((i - firstDayIndex) + 1)).toString())
		  }
		class:active={i === today.dayNumber+(firstDayIndex-1) &&
		monthIndex === today.month &&
		year === today.year}>
		  <!-- {(i - firstDayIndex) + 1} -->
		  <button 
			class="btn btn-sm" 
			on:click={exportInfoData(year, monthIndex+1, (i - firstDayIndex) + 1)}
			data-bs-toggle="modal" 
			data-bs-target="#Modal"
			>  
			{(i - firstDayIndex) + 1}
			<br>
			{#each worked_list as worked}
			{#if 
			  worked.year === year && 
        worked.month === (monthIndex+1) &&                            
			  worked.day === ((i - firstDayIndex) + 1) && 
			  workedDays.includes((worked.year*10000 + worked.month*100 + worked.day).toString())
        }  <!--일한날 포함 여부 확인 -->
			<!-- {#if worked.day === ((i - firstDayIndex) + 1) && worked.year === year && worked.month === (monthIndex+1)} -->
				{worked.note}<br>
        {#if worked.wage}
          {worked.wage.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}
        {/if}
			{/if}
			{/each}
		  </button>
	  </li>
	  <!-- <li class:active={i === today.dayNumber+(firstDayIndex-1) && monthIndex === today.month && year === today.year}>
		{(i - firstDayIndex) + 1}<br>
	  </li> -->
	  {/if}
	  {/each}
	</div>
	<div class="row check-input">
	  {#each workedPlaces as workedPlace}
	  <div class="col form-check">
		<input class="form-check-input" type="checkbox" value="{workedPlace}" bind:group={workedPlacesSelect} id="flexCheckDefault" >
		<label class="form-check-label" for="flexCheckDefault" >
		  {workedPlace}
		</label>
	  </div>
	  {/each}
	</div>
	<div class="row total">
	  <div class="col">
		total: {workedDays.length}
	  </div>
	  <!-- {workedPlacesSelect} -->
	</div>
  
	
  
  <style>
	.row.total {
	  padding-left: 10px;
	  padding-right: 10px;
		  margin: 2px;
	}
	  .row.check-input {
		  
	  padding-left: 20px;
	  padding-right: 20px;
		  margin: 2px;
	  }
	  ul {
		  list-style-type: none;
		  justify-content: center;
	  }
  
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
  
	  /* .weekdays li {
		  
		  display: inline-block;
		  width: 13.6%;
		  width: 13%;
		  color: #666;
		  text-align: center;
		  font-size: 0.9rem;
	  } */
  
	  /* Days (1-31) */
	  .days {
		  margin: 0;
		  padding: 3px 0;
		  /* padding: 10px 0; */
		  background: #eee;
		  font-size: smaller;
  
	  }
	  /* .day {
		  font-size: smaller;
	  } */
  
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
		  font-size: smaller;
		  /* font-size: 1.2rem; */
		  color: #777;
		  cursor: pointer;
		  min-height: 70px;
	  }
  
	  /* Highlight the "current" day */
	  .active {
		  /* padding: 5px; */
		  background: #1abc9c;
		  color: white !important
	  }
	  .worked {
		  background-color: midnightblue;
		  color: white !important
	  }
	  .worked > .btn {
		  color: white !important
		  
	  }
  </style>