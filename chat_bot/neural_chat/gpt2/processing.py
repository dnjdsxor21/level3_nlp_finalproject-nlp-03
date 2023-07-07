from typing import List, Tuple
from neural_chat.craigslist import Event, Agent, Scenario


def format_dialog(context: Scenario, dialog: List[Tuple[Agent, str]] = None) -> str:
    """Takes context, dialog and optionally a list of agents for
    corresponding dialog. If agents is None, it is assumed to be
    alternating starting from Buyer.

    """
    title = context.title
    descriptioin = context.description
    context_p: str = f"판매 상품: {title}\n상품 설명: {descriptioin}"
    dialog_p: List[str] = [
        ("구매자: " if a == Agent.BUYER else "판매자: ") + d.strip() for a, d in dialog
    ]
    return context_p + "\n" + "<sep>".join(dialog_p) + "<sep>"


def format_event(event: Event, use_price=True) -> str:
    evs = event.get_events()
    return format_dialog(
        event.scenario,
        [
            (ev.agent, ev.data["price"].utterance if use_price else str(ev.event))
            for ev in evs
        ],
    )
